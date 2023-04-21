import os
import json
import uuid
import datetime
import socket
import struct
import random

input_dir = 'DecoySet'
output_dir = 'DecoySet_Augmented'

for root, dirs, files in os.walk(input_dir):
    for filename in files:
        # Create the output directory path
        input_path = os.path.join(root, filename)
        output_path = input_path.replace(input_dir, output_dir)
        output_dirname = os.path.dirname(output_path)
        if not os.path.exists(output_dirname):
            os.makedirs(output_dirname)

        with open(input_path, 'r') as f:
            data = f.readlines()

        for i in range(50):
            output_data = []
            
            new_ids = [
                str(uuid.uuid4()),
                str(uuid.uuid4()),
                str(uuid.uuid4())
            ]

            new_ip = socket.inet_ntoa(struct.pack('>I', random.randint(1, 0xffffffff)))

            indices = list(range(len(data)))
            random.shuffle(indices)

            for j in indices:
                record = json.loads(output_data[j])
                new_time = str(datetime.datetime.utcnow() + datetime.timedelta(seconds=random.randint(0, 100000)))
                new_timestamp = str(datetime.datetime.utcnow().timestamp() + random.randint(0, 100000))

                line = output_data[j]
                original_ids = [
                    record['honeypotid'],
                    record['customerid'],
                    record['honeyserverid']
                ]
                
                for k in range(len(original_ids)):
                    line = line.replace(original_ids[k], new_ids[k])

                line = line.replace(record['time'], new_time)
                line = line.replace(record['parsedMessage']['timestamp'], new_timestamp)
                line = line.replace(record['parsedMessage']['ip'], new_ip)
                
                output_data.append(line)

            output_filename = f'{filename.split(".")[0]}_{i}.json'
            output_path_i = os.path.join(output_dirname, output_filename)
            with open(output_path_i, 'w') as f:
                f.writelines(output_data)
