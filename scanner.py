#!/usr/bin/env python3
"""Multi-threaded TCP port scanner (v0.2).
For educational use only: scan only systems you own or have permission to test."""
import argparse
import socket
import time
from concurrent.futures import ThreadPoolExecutor


def scan_port(host, port, timeout):
    """Return the port number if it is open, otherwise None."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(timeout)
        return port if s.connect_ex((host, port)) == 0 else None


def service_name(port):
    try:
        return socket.getservbyport(port)
    except OSError:
        return "unknown"


def parse_args():
    p = argparse.ArgumentParser(description="Simple multi-threaded TCP port scanner")
    p.add_argument("host", help="target IP or hostname (only systems you own or may test)")
    p.add_argument("-s", "--start", type=int, default=1, help="first port (default 1)")
    p.add_argument("-e", "--end", type=int, default=1024, help="last port (default 1024)")
    p.add_argument("-t", "--threads", type=int, default=100, help="threads (default 100)")
    p.add_argument("--timeout", type=float, default=0.5, help="seconds per port (default 0.5)")
    return p.parse_args()


def main():
    args = parse_args()
    if not (1 <= args.start <= args.end <= 65535):
        raise SystemExit("Ports must satisfy 1 <= start <= end <= 65535")
    try:
        ip = socket.gethostbyname(args.host)
    except socket.gaierror:
        raise SystemExit(f"Could not resolve host: {args.host}")

    print(f"Scanning {args.host} ({ip}) ports {args.start}-{args.end} ...")
    began = time.perf_counter()
    try:
        with ThreadPoolExecutor(max_workers=args.threads) as pool:
            results = pool.map(lambda p: scan_port(ip, p, args.timeout),
                               range(args.start, args.end + 1))
            open_ports = sorted(p for p in results if p)
    except KeyboardInterrupt:
        raise SystemExit("\nScan cancelled.")

    print(f"\n{'PORT':<8}{'SERVICE'}")
    for port in open_ports:
        print(f"{port:<8}{service_name(port)}")
    print(f"\n{len(open_ports)} open port(s) found in {time.perf_counter() - began:.2f}s")


if __name__ == "__main__":
    main()
