import pyshark
import matplotlib.pyplot as plt
from collections import Counter

pcap_file = r"C:\Program Files\Wireshark\first.pcapng"

capture = pyshark.FileCapture(pcap_file)

protocol_counts = Counter()

print("\n📊 Extracting packet protocols...\n")

for packet in capture:
    try:
        protocol = packet.highest_layer  
        protocol_counts[protocol] += 1  

    except AttributeError:
        continue  
capture.close()


plt.figure(figsize=(10, 6))
plt.bar(protocol_counts.keys(), protocol_counts.values(), color='skyblue')
plt.xlabel("Protocol")
plt.ylabel("Number of Packets")
plt.title("Network Traffic Analysis - Protocol Distribution")
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)


plt.show()
