import pyshark

pcap_file = r"C:\Program Files\Wireshark\first.pcapng"

suspicious_ports = [21, 22, 23, 25, 53, 110, 143, 3389, 4444]


capture = pyshark.FileCapture(pcap_file)

print("\n🔍 Scanning for suspicious packets...\n")
print("=" * 60)


for packet in capture:
    try:
       
        protocol = packet.transport_layer  
        src_ip = packet.ip.src
        dst_ip = packet.ip.dst
        src_port = int(packet[protocol].srcport)
        dst_port = int(packet[protocol].dstport)

        if dst_port in suspicious_ports:
            print(f"[🚨 ALERT] Suspicious packet detected!")
            print(f"🔹 Source IP: {src_ip} -> Destination IP: {dst_ip}")
            print(f"🔹 Protocol: {protocol}, Port: {dst_port}")
            print(f"🔹 Packet Length: {packet.length} bytes")
            print("-" * 60)
    
    except AttributeError:
        continue

print("\n✅ Scan complete.")
