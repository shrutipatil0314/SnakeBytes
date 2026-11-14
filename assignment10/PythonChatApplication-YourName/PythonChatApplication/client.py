import queue
import socket
import threading
import time
import tkinter as tk

from layout import BUFFER_SIZE, DEFAULT_HOST, DEFAULT_PORT, ChatLayout, parse_address

MAX_ATTEMPTS = 20       


def close_quietly(sock):
    """Close a socket and ignore errors if it is already closed."""
    if sock is None:
        return
    try:
        sock.shutdown(socket.SHUT_RDWR)
    except OSError:
        pass
    try:
        sock.close()
    except OSError:
        pass


class ChatClient:
    def __init__(self, root, host, port):
        self.root = root
        self.host = host
        self.port = port

        self.sock = None
        self.lock = threading.Lock()
        self.events = queue.Queue()     
        self.running = True

        self.ui = ChatLayout(root, "Client", self.send_message, x=500, y=80)
        root.protocol("WM_DELETE_WINDOW", self.close)

        self.ui.set_status("connecting...", "orange")
        threading.Thread(target=self._connect_and_listen, daemon=True).start()
        self.root.after(100, self.process_events)

 
    def _connect_and_listen(self):
        """Connect to the server, then keep receiving messages."""
        sock = None
        for attempt in range(MAX_ATTEMPTS):
            if not self.running:
                return
            try:
                sock = socket.create_connection((self.host, self.port), timeout=3)
                break
            except OSError:
                if attempt == 0:
                    self.events.put(("info", f"No server found at {self.host}:{self.port}, "
                                             "trying again..."))
                time.sleep(1)

        if sock is None:
            self.events.put(("info", "Could not reach the server. Start server.py, "
                                     "then restart the client."))
            self.events.put(("status", "not connected", "red"))
            return

        sock.settimeout(None)          
        with self.lock:
            if not self.running:
                close_quietly(sock)
                return
            self.sock = sock

        self.events.put(("info", f"Connected to the server at {self.host}:{self.port}"))
        self.events.put(("status", "connected", "green"))

        buffer = b""
        try:
            while True:
                data = sock.recv(BUFFER_SIZE)
                if not data:          
                    break
                buffer += data
           
                while b"\n" in buffer:
                    line, buffer = buffer.split(b"\n", 1)
                    text = line.decode("utf-8", errors="replace")
                    if text:
                        self.events.put(("received", f"Server: {text}"))
        except OSError:
            pass
        finally:
            with self.lock:
                if self.sock is sock:
                    self.sock = None
            close_quietly(sock)
            if self.running:
                self.events.put(("info", "The server closed the connection."))
                self.events.put(("status", "disconnected", "red"))

    
    def send_message(self, text):
        """Send text to the server. Returns True if it was sent."""
        with self.lock:
            sock = self.sock
        if sock is None:
            self.ui.add_message("[Not connected, so nothing was sent]", "info")
            return False
        try:
            sock.sendall(text.encode("utf-8") + b"\n")
        except OSError:
            self.ui.add_message("[Could not send, the connection was lost]", "info")
            return False
        self.ui.add_message(f"Client: {text}", "sent")
        return True

    def process_events(self):
        """Show whatever the background thread has queued up."""
        try:
            while True:
                event = self.events.get_nowait()
                if event[0] == "received":
                    self.ui.add_message(event[1], "received")
                elif event[0] == "info":
                    self.ui.add_message(event[1], "info")
                elif event[0] == "status":
                    self.ui.set_status(event[1], event[2])
        except queue.Empty:
            pass
        if self.running:
            self.root.after(100, self.process_events)

    def close(self):
        """Called when the window is closed."""
        self.running = False
        with self.lock:
            sock, self.sock = self.sock, None
        close_quietly(sock)
        self.root.destroy()


def main(host=DEFAULT_HOST, port=DEFAULT_PORT):
    root = tk.Tk()
    ChatClient(root, host, port)
    root.mainloop()


if __name__ == "__main__":
    main(*parse_address("Chat client"))
