from scapy.all import sniff, IP, TCP, UDP, Raw

def packet_callback(packet):
    print("\n--- Packet Captured ---")

    # Check if packet has IP layer
    if packet.haslayer(IP):
        ip = packet[IP]
        print("Source IP:", ip.src)
        print("Destination IP:", ip.dst)
        print("Protocol:", ip.proto)

        # TCP packets
        if packet.haslayer(TCP):
            tcp = packet[TCP]
            print("Protocol: TCP")
            print("Source Port:", tcp.sport)
            print("Destination Port:", tcp.dport)

        # UDP packets
        elif packet.haslayer(UDP):
            udp = packet[UDP]
            print("Protocol: UDP")
            print("Source Port:", udp.sport)
            print("Destination Port:", udp.dport)

        # Payload (application data)
        if packet.haslayer(Raw):
            payload = bytes(packet[Raw].load) # shows application layer data in bytes
            print("Payload size:", len(payload))
            print("Payload (first 40 bytes):", payload[:40])

    else:
        print("Non-IP packet")

# sniffing
print(("\n"))
print("🔍 Starting packet sniffing... Press Ctrl+C to stop.")

print("Enter the number of packets to capture or leave blank for continuous capture:")
user_input = input().strip()

#check for valid packet type
valid_filters = {"tcp" : "tcp", "udp" : "udp", "all" : "tcp or udp"}
print("Enter type of packet you want to capture (tcp/udp/all): ")
packet_type = input().strip().lower()

if packet_type not in valid_filters:
    print("Invalid packet type. please enter valid type (tcp/udp/all).")
    exit(1)
    
filtered = valid_filters[packet_type]

if user_input.isdigit():
    count = int(user_input)
    print(f"Capturing {count} packets...")
    sniff(filter=filtered, prn=packet_callback, count=count)
else:
    print("Capturing packets continuously...")
    sniff(filter=filtered, prn=packet_callback)
