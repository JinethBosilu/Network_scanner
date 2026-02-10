# Network Scanner

A small ARP network scanner that uses Scapy to discover hosts on a local network.

Purpose
- Scans an IP range and prints each discovered host's IP and MAC address.

Requirements
- Python 3
- scapy (install with `pip install scapy`)
- On Windows: run the script with Administrator privileges and install Npcap/WinPcap for packet sending.

Usage
1. Open a terminal in the `Network_scanner` folder.
2. Run:

```
python network_scanner.py
```

3. When prompted, enter the IP range to scan (CIDR notation like `192.168.1.0/24` is recommended).

Example input
- `192.168.1.0/24`

Notes
- The script uses ARP requests, so it only discovers hosts on the local network segment.
- Increase the `timeout` in the script if you need to wait longer for replies.
