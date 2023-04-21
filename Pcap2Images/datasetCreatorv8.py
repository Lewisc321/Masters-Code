# -*- coding: utf-8 -*-
"""
Created on Mon Apr 10 03:02:45 2023

@author: callu
"""

import os
import shutil
import random
from tqdm import tqdm



import os
import random

from PIL import Image
import os
import random

import numpy as np
import random


def group_categories(fileName):
    fileName = fileName.lower()
    if 'botnet' in fileName:
        return 'BotNet-Recruitment'
    elif 'censys' in fileName:
        return 'censys-inspect'
    elif 'expanse' in fileName:
        return 'Expanse'
    elif 'exploitation' in fileName:
        return 'Exploitation'
    return 'Other'

#'BotNet-Recruitment','censys-inspect','Expanse','Exploitation','Other'
def insert_random_errors(file_path):
    # Load image file
    image = Image.open(file_path)

    # Define parameters for random error insertion
    num_errors = int(image.size[0] * image.size[1] * 0.1)  # 10% of pixels
    error_value = random.randint(0, 255)

    # Insert random errors
    pixels = image.load()
    for i in range(num_errors):
        x = random.randint(0, image.size[0] - 1)
        y = random.randint(0, image.size[1] - 1)
        pixel_value = pixels[x, y]
        if isinstance(pixel_value, int):  # Grayscale image
            if pixel_value != error_value:
                pixels[x, y] = error_value
        elif isinstance(pixel_value, tuple):  # Color image
            error_tuple = tuple([error_value] * len(pixel_value))
            if pixel_value != error_tuple:
                pixels[x, y] = error_tuple

    # Save modified image to file
    filename = group_categories(file_path) + os.path.basename(file_path)
    new_file_name = f"Error_{filename}"
    new_file_path = os.path.join('Errored_Images', new_file_name)
    image.save(new_file_path)
    
    return new_file_path



def extract_balanced_datasets(root_folders, num_records, train_ratio, valid_ratio, test_ratio, num_datasets, error):
    # Find all files in the datapool and group them by category
    categories = {'BotNet-Recruitment':[],'censys-inspect':[],'Expanse':[],'Exploitation':[],'Other':[]}
    for root_folder in root_folders:
        for root, dirs, files in os.walk(root_folder):
            for file in files:
                category = group_categories(os.path.join(root, file))
                categories[category].append(os.path.join(root, file))

    # Calculate the number of records to extract for each category
    num_categories = len(categories)  # Number of categories
    num_records_per_category = (num_records // num_categories)*num_datasets
    print(f"Records per category: {num_records_per_category}")
    
    # Select the samples for this dataset
    all_files = []
    train_files = []
    valid_files = []
    test_files = []
    for category in ['BotNet-Recruitment','censys-inspect','Expanse','Exploitation','Other']:
        random.shuffle(categories[category])
        files = categories[category][:num_records_per_category*num_datasets]
        train_files.extend(files[:int(len(files) * train_ratio)])
        valid_files.extend(files[int(len(files) * train_ratio):int(len(files) * (train_ratio + valid_ratio))])
        test_files.extend(files[int(len(files) * (train_ratio + valid_ratio)):int(len(files) * (train_ratio + valid_ratio +test_ratio))])
    
    # Loop through each dataset and select the samples
    for i in range(num_datasets):
        train_dir = os.path.join('Datasets', 'DecoyDatasetv8_', f'Dataset{i+1}', 'train')
        valid_dir = os.path.join('Datasets', 'DecoyDatasetv8', f'Dataset{i+1}', 'valid')
        test_dir = os.path.join('Datasets', 'DecoyDatasetv8', f'Dataset{i+1}', 'test')
        os.makedirs(train_dir, exist_ok=True)
        os.makedirs(valid_dir, exist_ok=True)
        os.makedirs(test_dir, exist_ok=True)

        # Shuffle the files for each dataset
        random.shuffle(train_files)
        random.shuffle(valid_files)
        random.shuffle(test_files)

        # Select the samples for this dataset
        dataset_files = train_files[:int(num_records* train_ratio)]
        dataset_files.extend(valid_files[:int(num_records*valid_ratio)])
        dataset_files.extend(test_files[:int(num_records* test_ratio)])

        # Shuffle the samples for this dataset
        random.shuffle(dataset_files)
        # First progress bar for all files
        with tqdm(total=len(dataset_files), desc=f"Copying files for Dataset {i+1}") as pbar:        
            # Apply errors to the images if error=True
            # Copy the files to their respective directories
            for file in dataset_files:
                pbar.update(1)
                filename = os.path.basename(file)
                cat = group_categories(file)
                if file in train_files:
                    dest_dir = train_dir
                elif file in valid_files:
                    dest_dir = valid_dir
                elif file in test_files:
                    dest_dir = test_dir
                if error:
                    file = insert_random_errors(file) 
                path = os.path.join(dest_dir, cat)
                os.makedirs(path, exist_ok=True)
                shutil.copy(file, os.path.join(path, filename))
                    
        print(f"Dataset {i+1} extraction complete.")
        
root_folder = ['DecoyDataPool_img']
num_records = 15000
train_ratio = 0.7
valid_ratio = 0.2
test_ratio = 0.1
num_datasets = 10#0

extract_balanced_datasets(root_folder, num_records, train_ratio, valid_ratio, test_ratio, num_datasets, False)