import pyshark
capture = pyshark.FileCapture(r"C:\Program Files\Wireshark\first.pcapng")


print("=== PACKET SUMMARY ===\n")
for i, packet in enumerate(capture):
    try:
        print(f"Packet {i+1}:")
        print(f"Timestamp: {packet.sniff_time}")
        print(f"Source IP: {packet.ip.src}")
        print(f"Destination IP: {packet.ip.dst}")
        print(f"Protocol: {packet.transport_layer}")  
        print(f"Length: {packet.length} bytes")
        print("-" * 50)
        
        if i == 9:  
            break
    except AttributeError:
        continue  
