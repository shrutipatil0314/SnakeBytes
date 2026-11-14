import argparse
import subprocess
import sys
import time
from pathlib import Path

from layout import DEFAULT_HOST, DEFAULT_PORT


def run_both(host, port):
    
    folder = Path(__file__).resolve().parent
    options = ["--host", host, "--port", str(port)]

    server = subprocess.Popen([sys.executable, str(folder / "server.py"), *options])
    time.sleep(1)      
    client = subprocess.Popen([sys.executable, str(folder / "client.py"), *options])

    try:
        server.wait()
        client.wait()
    except KeyboardInterrupt:
        server.terminate()
        client.terminate()


def main():
    parser = argparse.ArgumentParser(description="Python socket chat application")
    parser.add_argument("mode", nargs="?", choices=["server", "client", "both"],
                        default="both", help="what to start (default: both)")
    parser.add_argument("--host", default=DEFAULT_HOST,
                        help=f"address to use (default {DEFAULT_HOST})")
    parser.add_argument("--port", type=int, default=DEFAULT_PORT,
                        help=f"port to use (default {DEFAULT_PORT})")
    args = parser.parse_args()

    if args.mode == "server":
        import server
        server.main(args.host, args.port)
    elif args.mode == "client":
        import client
        client.main(args.host, args.port)
    else:
        run_both(args.host, args.port)


if __name__ == "__main__":
    main()
