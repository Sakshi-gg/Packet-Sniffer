import pyshark

capture = pyshark.FileCapture(r"C:\Program Files\Wireshark\first.pcapng")
count = 0
for packet in capture:
    print(packet)
    print("-" * 50)
    count += 1
    if count == 10:  
        break