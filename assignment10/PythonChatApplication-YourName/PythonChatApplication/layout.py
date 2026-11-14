import argparse
import tkinter as tk
from tkinter import scrolledtext

DEFAULT_HOST = "127.0.0.1"   
DEFAULT_PORT = 5050
BUFFER_SIZE = 1024


def parse_address(description):
    """Read --host and --port from the command line (both are optional)."""
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument("--host", default=DEFAULT_HOST,
                        help=f"address to use (default {DEFAULT_HOST})")
    parser.add_argument("--port", type=int, default=DEFAULT_PORT,
                        help=f"port to use (default {DEFAULT_PORT})")
    args = parser.parse_args()
    return args.host, args.port


class ChatLayout:

    def __init__(self, root, title, on_send, x=100, y=100):
        """
        root     - the Tk() window
        title    - text for the title bar ("Server" or "Client")
        on_send  - function called with the typed text; it should return True
                   if the message was sent, so the entry can be cleared
        x, y     - where the window appears on the screen
        """
        self.root = root
        self.on_send = on_send

        root.title(title)
        root.geometry(f"420x480+{x}+{y}")
        root.minsize(320, 360)

    
        self.status_label = tk.Label(root, text="Status: starting...", anchor="w",
                                     font=("Arial", 10, "bold"), fg="gray")
        self.status_label.pack(fill=tk.X, padx=10, pady=(10, 4))

       
        self.chat_box = scrolledtext.ScrolledText(
            root, state="disabled", wrap=tk.WORD, font=("Consolas", 10), bg="white")
        self.chat_box.pack(fill=tk.BOTH, expand=True, padx=10, pady=4)
        self.chat_box.tag_config("sent", foreground="#1a56db")
        self.chat_box.tag_config("received", foreground="#0f7b3f")
        self.chat_box.tag_config("info", foreground="gray",
                                 font=("Consolas", 9, "italic"))

   
        bottom = tk.Frame(root)
        bottom.pack(fill=tk.X, padx=10, pady=(4, 10))

        self.entry = tk.Entry(bottom, font=("Arial", 11))
        self.entry.pack(side=tk.LEFT, fill=tk.X, expand=True, ipady=4)
        self.entry.bind("<Return>", self._send_clicked) 

        self.send_button = tk.Button(bottom, text="Send", width=8,
                                     command=self._send_clicked)
        self.send_button.pack(side=tk.RIGHT, padx=(8, 0))

        self.entry.focus_set()

    def _send_clicked(self, event=None):
        text = self.entry.get().strip()
        if not text:
            return
        if self.on_send(text):
            self.entry.delete(0, tk.END)

    def add_message(self, text, kind="info"):
        """Add a line to the message box. kind is 'sent', 'received' or 'info'."""
        self.chat_box.config(state="normal")
        self.chat_box.insert(tk.END, text + "\n", kind)
        self.chat_box.config(state="disabled")
        self.chat_box.see(tk.END)

    def set_status(self, text, color="gray"):
        self.status_label.config(text=f"Status: {text}", fg=color)
