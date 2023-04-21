# -*- coding: utf-8 -*-
"""
Created on Mon Jan 16 18:33:19 2023

@author: Callum Manning

Strath Uni - 201720173
"""
#My Modules
import sys
import re
from scapy.all import *
from memory_profiler import profile
from UserSetUp import *
from PIL import Image
import numpy as np
from pprint import pprint
from tqdm import tqdm


RGBpixels = []
Graypixels =[]

def extendbyte(start, end,bi):
     return int((int(bi[start:end],2)/8) * 2**8)

def gray2rgb(byte):
     bi = format(byte,'08b').replace("0b", "")
     r = extendbyte(0,3,bi)
     g = extendbyte(2,5,bi)
     b = extendbyte(7,8,bi)
     return([r,g,b])

def createArray(fileName):
    Graypixels =[]
    RGBpixels =[]
    with open(fileName, 'rb') as fp:
        for byte_s in fp:
            for byte in byte_s:
                byte = byte + 1
                if byte > 255: 
                    byte = 255;
                Graypixels.append(byte)        
                RGBpixels.append(gray2rgb(byte ))
        if len(Graypixels)>=max_Pixels:
            print('Failed to Convert, too big')
            return(0,0)
        return(Graypixels, RGBpixels)


def paddArraystoMatrix(gray, colour):
    #print(len(gray))
    #print(len(colour))
    rgb_padded =[]
    gray_padded = []
    rgb_padded =list(colour)
    gray_padded = list(gray)
    if len(gray)<max_Pixels:
        padding = max_Pixels-len(gray)
        #print(padding)
        gray_padded.extend(np.zeros(padding))
        for _ in range(padding):
            rgb_padded.append([0,0,0])
    rgb_padded = np.array(rgb_padded, dtype=np.uint8).reshape((pixelDimen, pixelDimen, 3))
    gray_padded = np.array(gray_padded, dtype=np.uint8).reshape((pixelDimen, pixelDimen))
    return (gray_padded, rgb_padded)

def JSON2_Image(PCAP_file_path, PCAP_Name):
    Gray_array = []
    RGB_array =[]
    Gray_array_padded=[]
    RGB_array_padded =[]
    [Gray_array, RGB_array] = createArray(PCAP_file_path)
    if type(RGB_array) is int:
        failedArray = PCAP_file_path
        return failedArray, None
    [Gray_array_padded, RGB_array_padded] = paddArraystoMatrix(Gray_array,RGB_array)
    if type(RGB_array_padded) is int:
        failedArray = PCAP_file_path
        return failedArray, None
    colour_image = Image.fromarray(RGB_array_padded, 'RGB')
    gray_image = Image.fromarray(Gray_array_padded)
    return colour_image, gray_image



def jsonDataset(input_dir, output_dir):
    image_extension = ".png"
    
    # Traverse the input directory structure
    for category_folder in os.listdir(input_dir):
        category_path = os.path.join(input_dir, category_folder)
        if os.path.isdir(category_path):
            with tqdm(total=len(os.listdir(category_path)), desc=f"Changing Json Files in {category_path}") as pbar:   
                for json_file in os.listdir(category_path):
                    pbar.update(1)
                    json_path = os.path.join(category_path, json_file)
                    if os.path.isfile(json_path) and json_path.endswith(".json"):
                        json_name = os.path.splitext(json_file)[0]
                        # Create an image from the JSON file contents
                        colour_image, gray_image = JSON2_Image(json_path, json_name)
                        if not colour_image or not gray_image:
                            print(f"Failed to create image from {json_path}")
                            continue
                        # Save the colour image in the corresponding category folder in the output directory
                        output_category_path = os.path.join(output_dir, category_folder)
                        if not os.path.exists(output_category_path):
                            os.makedirs(output_category_path)
                        colour_output_path = os.path.join(output_category_path, f"{json_name}{image_extension}")
                        colour_image.save(colour_output_path)
    
                        # Save the grayscale image in the corresponding category folder in the output directory
                        gray_output_path = os.path.join(output_category_path, f"{json_name}_gray{image_extension}")
                        gray_image.save(gray_output_path)



input_dir = 'DecoySet_Augmented/'
output_dir= 'DecoyDataPool_Img/'
jsonDataset(input_dir, output_dir)



