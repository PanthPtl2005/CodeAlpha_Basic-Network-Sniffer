# 🕵️ Basic Network Sniffer using Python & Scapy

A simple Python-based **network packet sniffer** built using **Scapy** to capture, filter, and analyze live network traffic.  
This project was developed as part of a **cybersecurity internship task** to understand how data flows across a network at the packet level.

---

## 📌 Features

- Captures live network packets from the system interface
- Supports filtering:
  - TCP packets
  - UDP packets
  - Both TCP and UDP
- Extracts and displays:
  - Source IP address
  - Destination IP address
  - Protocol type
  - Source and destination ports
  - Application-layer payload (if present)
- Option to capture a fixed number of packets or run continuously

---

## 🧠 Technologies Used

- **Python 3**
- **Scapy** (packet capture and analysis)

---

## 📂 Code Overview

### Core Scapy Components

| Component | Purpose |
|--------|--------|
| `sniff()` | Captures packets from the network |
| `IP` | Handles Network Layer (Layer 3) |
| `TCP` | Handles TCP packets (Layer 4) |
| `UDP` | Handles UDP packets (Layer 4) |
| `Raw` | Accesses application-layer payload |

---

## 📡 How Packet Capture Works

The core of the program is the `sniff()` function:

```python
sniff(filter=filtered, prn=packet_callback, count=count)
````

### Parameters Explained

* **filter**
  Uses Berkeley Packet Filter (BPF) syntax:

  * `tcp` → capture only TCP packets
  * `udp` → capture only UDP packets
  * `tcp or udp` → capture both

* **prn**
  Callback function (`packet_callback`) executed for every captured packet.

* **count**

  * If specified: captures a fixed number of packets
  * If omitted: captures packets continuously until stopped manually

**Flow:**
Capture packet → Pass to callback → Analyze → Display output

---

## 🌐 IP Packet Analysis (Layer 3)

* Checks if the packet contains an IP layer
* Extracts:

  * Source IP address
  * Destination IP address
  * Protocol number (TCP = 6, UDP = 17)
* Helps identify communication between hosts

---

## 🚚 TCP & UDP Packet Analysis (Layer 4)

### TCP Packets

* Displays:

  * Source port
  * Destination port
* Useful for identifying services like:

  * HTTP / HTTPS (80 / 443)
  * SSH (22)
  * FTP, Mail protocols

### UDP Packets

* Displays:

  * Source port
  * Destination port
* Common in:

  * DNS
  * Streaming services
  * VoIP
  * Connectionless communication

---

## 📦 Payload Inspection (Application Layer)

* Extracts raw application data if available
* Displays:

  * Payload size
  * First 40 bytes of payload for inspection
* Shows actual transmitted data (plain or encrypted)

---

## ⚠️ Permissions Required

Packet sniffing requires **privileged access** on most systems.

### Linux / Unix / macOS

Run the script using:

```bash
sudo python3 network_sniffer.py
```

Without elevated privileges, packet capture may fail.

---

## 🚀 How to Run

1. Install dependencies:

```bash
pip install scapy
```

2. Run the program:

```bash
sudo python3 network_sniffer.py
```

3. Enter:

   * Number of packets to capture (or leave blank for continuous capture)
   * Packet type to filter (`tcp`, `udp`, or `all`)

---

## 🎯 Learning Outcomes

* Practical understanding of:

  * TCP/IP and OSI models
  * Packet structure and flow
  * Transport and application layer data
* Hands-on experience with packet sniffing fundamentals
* Strong foundation for ethical hacking and network security analysis

---

## 📜 Disclaimer

This project is for **educational purposes only**.
Do not use packet sniffing techniques on networks without proper authorization.

---

## 📌 Author

**Panth Patel**

