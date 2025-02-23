import pyshark
import logging

logging.basicConfig(
    filename="network_log.csv",  
    level=logging.INFO,  
    format="%(asctime)s, %(message)s",  
    datefmt="%Y-%m-%d %H:%M:%S"
)

logging.info("Timestamp, Protocol, Source IP, Destination IP, Length")

capture = pyshark.FileCapture(r"C:\Program Files\Wireshark\first.pcapng")

for packet in capture:
    try:
        protocol = packet.highest_layer
        src_ip = packet.ip.src if hasattr(packet, "ip") else "Unknown"
        dst_ip = packet.ip.dst if hasattr(packet, "ip") else "Unknown"
        length = packet.length if hasattr(packet, "length") else "Unknown"
        
        logging.info(f"{protocol}, {src_ip}, {dst_ip}, {length}")

    except Exception as e:
        logging.error(f"Error processing packet: {e}")

print("✅ Network traffic logged in 'network_log.csv'.")
