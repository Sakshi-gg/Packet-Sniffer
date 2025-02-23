# Packet-Sniffer
This project is a Packet_Sniffer that captures network packets, analyzes their contents, and generates reports. It helps identify potential security threats and unusual traffic patterns.
# Features

✅ Packet Capture: Reads network packets from a .pcapng file.

✅ Suspicious Packet Detection: Flags unusual packets based on predefined rules.

✅ Data Visualization: Graphical representation of network traffic trends.

✅ Logging & Reporting: Generates PDF reports of network activity.

# Installation & Setup

## Prerequisites -

Ensure you have Python 3.11+ installed along with the following dependencies:
 ```bash
pip install pyshark fpdf pandas matplotlib
  ```
# Running the Project

## Capture Network Packets 
 ```bash
python packet_capture.py first.pcapng
  ```
## Detect Suspicious Packets
 ```bash
python suspicious_detection.py
  ```
## Generate PDF Report-
 ```bash
python logging_report.py
  ```
# Contact
For any questions or suggestions, please open an issue or contact me at your sakshigumaste@gmail.com
