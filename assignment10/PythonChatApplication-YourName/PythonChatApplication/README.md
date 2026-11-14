# Python Chat Application

This is my socket programming assignment. It's a small chat app where a **server** and a **client** talk to each other over a network connection. Both have their own window, and either side can send a message at any time. Messages show up in both windows.

I used Python's `socket` module for the connection and `tkinter` for the windows. Nothing needs to be installed, because both come with Python.

## Files

| File | What it does |
|------|--------------|
| `server.py` | The server. Opens a window, waits for a client to connect, then sends and receives messages |
| `client.py` | The client. Opens a window, connects to the server, then sends and receives messages |
| `layout.py` | The chat window itself (status line, message box, entry field, Send button). Both the server and the client use it, so I only wrote it once |
| `main.py` | The easy way to start everything with one command |

## How to run it

You need Python 3 with Tkinter (it's included in the normal Windows and Mac installers from python.org).

**The quick way (one command, both windows):**

```
python main.py
```

This opens the server window and then the client window next to it. They connect by themselves.

**The way I did it for the screenshots (two terminals):**

1. In the first terminal, start the server:
   ```
   python server.py
   ```
2. In a second terminal, start the client:
   ```
   python client.py
   ```

Start the server first. (If you start the client first, it keeps trying for about 20 seconds, so it still works if you're quick.)

Then type something in either window and press **Enter** or click **Send**. The message appears in both windows.

On Mac or Linux you may need `python3` instead of `python`.

## What you should see

- The server window says *waiting for a client...* and then turns green with *client connected*.
- The client window says *connected* in green.
- If the client types `Hi, I am Amit.`, both windows show `Client: Hi, I am Amit.`
- If the server answers `Hello Amit, I am Harshit.`, both windows show `Server: Hello Amit, I am Harshit.`

My own messages are shown in blue and messages I receive are shown in green, so it's easy to tell them apart.

## How it works

1. **The server** creates a socket, `bind()`s it to an address and port (127.0.0.1, port 5050) and calls `listen()`. Then `accept()` waits for a client.
2. **The client** creates a socket and calls `connect()` to the same address and port.
3. Once they're connected, each side uses `sendall()` to send and `recv()` to receive.

A few things I had to think about:

- **Threads.** `accept()` and `recv()` wait until something happens. If they ran in the main program, the window would freeze. So each side receives messages in a background thread.
- **Queue.** Tkinter windows can only be changed from the main thread. So the background threads put what they receive into a `queue.Queue`, and the window checks the queue every 100 ms and shows the new messages. (My Module 22 notes recommend exactly this.)
- **Newline at the end of each message.** TCP is a stream of bytes, so one `recv()` can return half a message, or two messages stuck together. I add a `\n` to the end of every message and split on it when receiving. I tested sending 50 messages very quickly and none got joined or lost.
- **One client at a time.** If a second client tries to connect while one is chatting, it gets a "server is busy" message. When the first client leaves, the server waits for the next one.
- **Cleaning up.** Closing a window closes its sockets properly. If one side leaves, the other side shows a message instead of crashing.

## Using two computers

By default everything runs on one computer (127.0.0.1 means "this computer"). To chat between two computers on the same Wi-Fi or network:

1. On the server computer, start the server so it accepts outside connections:
   ```
   python main.py server --host 0.0.0.0
   ```
2. Find that computer's IP address (`ipconfig` on Windows, `ifconfig` or `ip a` on Mac/Linux), for example `192.168.1.20`.
3. On the other computer, start the client with that address:
   ```
   python main.py client --host 192.168.1.20
   ```

The firewall may ask for permission the first time. You can also change the port with `--port 6000` (use the same number on both sides).

## Problems you might run into

- **"Could not start the server"**: something is already using port 5050, probably another copy of the server. Close it or use `--port`.
- **The client says "No server found"**: the server isn't running yet, or the host/port don't match.
- **`No module named tkinter`** (Linux): install it with `sudo apt install python3-tk`.

## Things I'd add with more time

- Several clients chatting at once (a group chat)
- Usernames instead of just "Client" and "Server"
- Timestamps next to each message
