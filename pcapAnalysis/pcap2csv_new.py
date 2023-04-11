import os
from scapy.all import *
import csv

pcap_dir = '/Users/lewis/Desktop/Uni/5th_Year/EM501/Data/Pcap/'
csv_dir = '/Users/lewis/Desktop/Uni/5th_Year/EM501/Data/Pcap/CSV'

if not os.path.exists(csv_dir):
    os.makedirs(csv_dir)

for filename in os.listdir(pcap_dir):
    if filename.endswith('.pcap'):
        packets = rdpcap(os.path.join(pcap_dir, filename))

        packet_list = []
        for packet in packets:
            # Check if both IP and TCP layers exist in the packet
            if packet.haslayer(IP) and packet.haslayer(TCP):
                packet_dict = {
                    'source_ip': packet[IP].src,
                    'destination_ip': packet[IP].dst,
                    'source_port': packet[TCP].sport,
                    'destination_port': packet[TCP].dport,
                    'protocol': packet[IP].proto
                }
                packet_list.append(packet_dict)

        csv_filename = os.path.splitext(filename)[0] + '.csv'
        csv_path = os.path.join(csv_dir, csv_filename)
        with open(csv_path, 'w') as f:
            writer = csv.DictWriter(f, fieldnames=['source_ip', 'destination_ip', 'source_port', 'destination_port', 'protocol'])
            writer.writeheader()
            writer.writerows(packet_list)