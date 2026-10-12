#!/usr/bin/env python3
"""Simple TCP port scanner (v0.1).
For educational use only: scan only systems you own or have permission to test."""
import socket


def scan_port(host, port, timeout=0.5):
    """Return True if the TCP port is open."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(timeout)
        return s.connect_ex((host, port)) == 0


def main():
    host = "127.0.0.1"  # your own machine
    print(f"Scanning {host} ...")
    for port in range(1, 1025):
        if scan_port(host, port):
            print(f"Port {port} is open")
    print("Done.")


if __name__ == "__main__":
    main()
