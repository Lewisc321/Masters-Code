# -*- coding: utf-8 -*-
"""
Created on Thu Apr  6 13:44:26 2023

@author: callu - Callum Manning 

Strathclyde Student Reg: 201720173
"""



import os
import json
import shutil

count = 0
root_folder = 'apache-server1'
for root, dirs, files in os.walk(root_folder):
    if "attacker.json" in files:
        attacker_path = os.path.join(root, "attacker.json")
        # with open(attacker_path, "r") as f:
        #     attacker_data = json.load(f)
        # ttps = attacker_data.get("TTPs", [])
        # for ttp in ttps:
        #     ttp_folder = os.path.join('DecoySet', ttp)
        #     print(ttp_folder)
        #     if not os.path.exists(ttp_folder):
        #         os.mkdir(ttp_folder)
        for file in files:
            if file != "attacker.json":
                print(file)
                count =count+1
        print('\n')
print(count)
