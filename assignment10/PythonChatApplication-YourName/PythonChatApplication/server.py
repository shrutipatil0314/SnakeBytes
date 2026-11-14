import queue
import socket
import sys
import threading
import tkinter as tk
from tkinter import messagebox

from layout import BUFFER_SIZE, DEFAULT_HOST, DEFAULT_PORT, ChatLayout, parse_address


def close_quietly(sock):
   
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


class ChatServer:
    def __init__(self, root, host, port):
        self.root = root
        self.host = host
        self.port = port

        self.listener = None            
        self.conn = None                
        self.conn_lock = threading.Lock()
        self.events = queue.Queue()     
        self.running = True

        self.ui = ChatLayout(root, "Server", self.send_message, x=60, y=80)
        root.protocol("WM_DELETE_WINDOW", self.close)

        if not self.start_listening():
            return
        self.root.after(100, self.process_events)

   
    def start_listening(self):
       
        try:
            self.listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            if sys.platform != "win32":
              
                self.listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            self.listener.bind((self.host, self.port))
            self.listener.listen(1)
        except OSError as error:
            messagebox.showerror(
                "Server error",
                f"Could not start the server on {self.host}:{self.port}\n\n{error}\n\n"
                "Is another copy of the server already running?")
            close_quietly(self.listener)
            self.listener = None
            self.running = False
            self.root.destroy()
            return False

        self.ui.set_status("waiting for a client...", "orange")
        self.ui.add_message(f"Server started on {self.host}:{self.port}", "info")
        self.ui.add_message("Waiting for a client to connect...", "info")

        threading.Thread(target=self._accept_loop, daemon=True).start()
        return True

    def _accept_loop(self):
       
        while self.running:
            try:
                sock, address = self.listener.accept()
            except OSError:
                break                  

            with self.conn_lock:
                busy = self.conn is not None
                if not busy:
                    self.conn = sock

            if busy:
                try:
                    sock.sendall(b"[Server is busy with another client]\n")
                except OSError:
                    pass
                close_quietly(sock)
                continue

            self.events.put(("info", f"Client connected from {address[0]}:{address[1]}"))
            self.events.put(("status", "client connected", "green"))
            threading.Thread(target=self._serve_client, args=(sock,), daemon=True).start()

    def _serve_client(self, sock):
       
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
                        self.events.put(("received", f"Client: {text}"))
        except OSError:
            pass
        finally:
            with self.conn_lock:
                if self.conn is sock:
                    self.conn = None
            close_quietly(sock)
            if self.running:
                self.events.put(("info", "Client disconnected. Waiting for a new client..."))
                self.events.put(("status", "waiting for a client...", "orange"))


    def send_message(self, text):
       
        with self.conn_lock:
            sock = self.conn
        if sock is None:
            self.ui.add_message("[No client is connected, so nothing was sent]", "info")
            return False
        try:
            sock.sendall(text.encode("utf-8") + b"\n")
        except OSError:
            self.ui.add_message("[Could not send, the connection was lost]", "info")
            return False
        self.ui.add_message(f"Server: {text}", "sent")
        return True

    def process_events(self):
  
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
      
        self.running = False
        with self.conn_lock:
            sock, self.conn = self.conn, None
        close_quietly(sock)
        close_quietly(self.listener)
        self.root.destroy()


def main(host=DEFAULT_HOST, port=DEFAULT_PORT):
    root = tk.Tk()
    ChatServer(root, host, port)
    root.mainloop()


if __name__ == "__main__":
    main(*parse_address("Chat server"))
