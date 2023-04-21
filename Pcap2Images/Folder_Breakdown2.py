# -*- coding: utf-8 -*-
"""
Created on Mon Apr  3 17:50:05 2023

@author: callu
"""

import os

def count_files(dir_path):
    """
    Recursively count the number of files in a directory and its subdirectories.
    """
    file_count = 0
    for dirpath, dirnames, filenames in os.walk(dir_path):
        for f in filenames:
            file_count += 1
    return file_count

def get_folder_file_counts(file_path):
    """
    Given a file path, read the list of folder addresses and return a list of tuples
    containing the folder address and the number of files in that folder.
    """
    folder_file_counts = []
    with open(file_path, 'r') as f:
        for line in f:
            if not '___' in line:
                if not '' == line:
                    folder_path = line.strip()
                    file_count = count_files(folder_path)
                    folder_file_counts.append((folder_path, file_count))
    return folder_file_counts

folder_file_counts = get_folder_file_counts('Folders.txt')
print(folder_file_counts)
