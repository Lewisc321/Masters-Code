"""""

@author: lewis


"""

import os
from scapy.all import *

# Set the directory where the pcap files are located
pcap_dir = '/Users/lewis/Desktop/Uni/5th_Year/EM501/Data/Pcap/BRUTEFORCEATTACKS'

# Set the directory where the csv files should be saved
csv_dir = '/Users/lewis/Desktop/Uni/5th_Year/EM501/Data/Pcap/CSV/BRUTEFORCEATTACKS'

# Create the csv directory if it does not exist
if not os.path.exists(csv_dir):
    os.makedirs(csv_dir)

# Loop through all the pcap files in the directory
for filename in os.listdir(pcap_dir):
    if filename.endswith('.pcap'):
        # Load the pcap file into memory
        packets = rdpcap(os.path.join(pcap_dir, filename))

        # Convert the packets to a list of dictionaries
        packet_list = []
        for packet in packets:
            packet_dict = {
                'source_ip': packet[IP].src,
                'destination_ip': packet[IP].dst,
                'source_port': packet[TCP].sport,
                'destination_port': packet[TCP].dport,
                'protocol': packet[IP].proto
            }
            packet_list.append(packet_dict)

        # Write the list of dictionaries to a csv file
        csv_filename = os.path.splitext(filename)[0] + '.csv'
        csv_path = os.path.join(csv_dir, csv_filename)
        with open(csv_path, 'w') as f:
            writer = csv.DictWriter(f, fieldnames=['source_ip', 'destination_ip', 'source_port', 'destination_port', 'protocol'])
            writer.writeheader()
            writer.writerows(packet_list)