# port-scanner

A fast, multi-threaded TCP port scanner written in Python, built as a learning project.

> **Ethical use only.** Scan only systems you own or have explicit written permission to test. Unauthorized scanning may be illegal.

## Features
- Scans any port range, default 1-1024
- Multi-threaded for fast scans
- Shows the common service name for each open port
- Handles invalid hosts, bad port ranges and Ctrl+C cleanly
- Pure standard library: no installs needed

## Requirements
- Python 3.8+

## Usage
```bash
python3 scanner.py <host> [options]
```

| Option | Description | Default |
|---|---|---|
| `-s`, `--start` | First port to scan | 1 |
| `-e`, `--end` | Last port to scan | 1024 |
| `-t`, `--threads` | Number of threads | 100 |
| `--timeout` | Seconds to wait per port | 0.5 |

### Examples
```bash
# Scan common ports on your own machine
python3 scanner.py 127.0.0.1

# Scan every port with more threads
python3 scanner.py 127.0.0.1 -s 1 -e 65535 -t 200
```

### Example output
```
Scanning 127.0.0.1 (127.0.0.1) ports 1-1024 ...

PORT    SERVICE
80      http

1 open port(s) found in 0.12s
```

## How it works
For each port the scanner tries a full TCP connection with `socket.connect_ex()`. If the connection succeeds, the port is open. A thread pool runs many of these checks in parallel.

## Roadmap
- [ ] Banner grabbing
- [ ] JSON / CSV output
- [ ] UDP scanning
- [ ] Scan multiple hosts

## License
MIT. See [LICENSE](LICENSE).
