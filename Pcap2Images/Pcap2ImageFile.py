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
        fp_Lines = fp.readlines()
        if len(fp_Lines)>=max_Pixels:
            print('Failed to Convert, too big')
            return(0,0)
        for byte in byte_s:
            byte = byte + 1
            if byte > 255: 
                byte = 255;
            Graypixels.append(byte)        
            RGBpixels.append(gray2rgb(byte ))
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
#

def PCAP2_Image(PCAP_file_path, PCAP_Name):
    Gray_array = []
    RGB_array =[]
    Gray_array_padded=[]
    RGB_array_padded =[]
    [Gray_array, RGB_array] = createArray(PCAP_file_path)
    if type(RGB_array) is int:
        failedArray = PCAP_file_path
        return failedArray
    [Gray_array_padded, RGB_array_padded] = paddArraystoMatrix(Gray_array,RGB_array)
    if type(RGB_array_padded) is int:
        failedArray = PCAP_file_path
        return failedArray
    colour_image = Image.fromarray(RGB_array_padded, 'RGB')
    #print(IMAGE_OUTPUT + PCAP_Name + colour_suffix)
    colour_image.save(IMAGE_OUTPUT + PCAP_Name + colour_suffix)
    gray_image = Image.fromarray(Gray_array_padded)
    gray_image.save(IMAGE_OUTPUT + PCAP_Name +  gray_suffix)



# Need a new strategy in Place 
# Open Buffer -> 36 by 36 with zeros 
# New byte added 
# Byte List from file
# If bytelist is greater than 36, 
# Offset is incurred and shift takes place
# Pass to padder
# Save each image
def createBufferImages(fileName, PCAP_Name, prev_buffer=[],prevBuffer_Name=None):
    if prevBuffer_Name == None:
        prevBuffer_Name = PCAP_Name 
    PCAP_file_path = fileName
    buffer_size = max_Pixels  # The size of our rolling buffer
    buffer = []  # Initialize the buffer as an empty list
    num_bytes = sum(len(line) for line in open(fileName, 'rb').readlines())
    lenLines = len(open(fileName, 'rb').readlines())
    if num_bytes > buffer_size:
        print("WARNING: Number of bytes in PCAP file exceeds buffer size.")
    i = 0
    if num_bytes> 7*buffer_size:
        print('FAILURE: File Too Large')
        return 'FAILURE: File Too Large'
    with open(fileName, 'rb') as fp:
        for byte_s in fp:
            for byte in byte_s:
                byte = byte + 1
                if byte > 255: 
                    byte = 255;
                buffer += [byte]  # Add 1 to each new byte and append to the end of the buffer
                prev_buffer += [byte]
                if len(buffer) > buffer_size:
                    buffer.pop(0)
                if len(prev_buffer)>buffer_size:
                    prev_buffer.pop(0)
            Graypixels = np.array(buffer, dtype=np.uint8)
            RGBpixels = [gray2rgb(byte) for byte in Graypixels]
            prevGraypixels = np.array(prev_buffer, dtype=np.uint8)
            prevRGBpixels = [gray2rgb(byte) for byte in prevGraypixels]
            [Gray_array_padded, RGB_array_padded] = paddArraystoMatrix(Graypixels, RGBpixels)
            [prev_Gray_array_padded, prev_RGB_array_padded] = paddArraystoMatrix(prevGraypixels, prevRGBpixels)
            if type(RGB_array_padded) is int:
                failedArray = PCAP_file_path
                return failedArray
            if type(prev_RGB_array_padded) is int:
                failedArray = PCAP_file_path
                return failedArray
            colour_image = Image.fromarray(RGB_array_padded, 'RGB')
            #print(IMAGE_OUTPUT_FRESH + PCAP_Name + str(i + 1) + colour_suffix)
            colour_image.save(IMAGE_OUTPUT_FRESH + PCAP_Name + str(i + 1) + colour_suffix)
            gray_image = Image.fromarray(Gray_array_padded)
            gray_image.save(IMAGE_OUTPUT_FRESH + PCAP_Name + str(i + 1) + gray_suffix)

            colour_image_continued = Image.fromarray(prev_RGB_array_padded, 'RGB')
            gray_image_continued = Image.fromarray(prev_Gray_array_padded)

            if i < round(int(1/3*lenLines)):
                 #print(IMAGE_OUTPUT_CONTINOUS + prevBuffer_Name + str(i + 1) + '_prev_buffer_' + colour_suffix)
                 colour_image_continued.save(IMAGE_OUTPUT_CONTINOUS + prevBuffer_Name +'_prev_buffer_'+ str(i + 1) + colour_suffix)
                 gray_image_continued.save(IMAGE_OUTPUT_CONTINOUS + prevBuffer_Name + '_prev_buffer_' + str(i + 1) + gray_suffix)
            else:
                 #print(IMAGE_OUTPUT_CONTINOUS + PCAP_Name + '_prev_buffer_'+ str(i + 1) + colour_suffix)
                 colour_image_continued.save(IMAGE_OUTPUT_CONTINOUS + PCAP_Name + '_prev_buffer_'+ str(i + 1) + colour_suffix)
                 gray_image_continued.save(IMAGE_OUTPUT_CONTINOUS + PCAP_Name + '_prev_buffer_'+ str(i + 1) + gray_suffix)
            i += 1
    colour_image.save(IMAGE_OUTPUT_FINAL + PCAP_Name + colour_suffix)
    gray_image.save(IMAGE_OUTPUT_FINAL + PCAP_Name  + gray_suffix)
    return [PCAP_Name, prev_buffer]


def createFinalImages(fileName, PCAP_Name):
    PCAP_file_path = fileName
    buffer_size = max_Pixels  # The size of our rolling buffer
    buffer = []  # Initialize the buffer as an empty list
    num_bytes = sum(len(line) for line in open(fileName, 'rb').readlines())
    lenLines = len(open(fileName, 'rb').readlines())
    if num_bytes > buffer_size:
        print("WARNING: Number of bytes in PCAP file exceeds buffer size.")
    i = 0
    if num_bytes> 7*buffer_size:
        print('FAILURE: File Too Large')
        return 'FAILURE: File Too Large'
    with open(fileName, 'rb') as fp:
        for byte_s in fp:
            for byte in byte_s:
                byte = byte + 1
                if byte > 255: 
                    byte = 255;
                buffer += [byte]  # Add 1 to each new byte and append to the end of the buffer
                if len(buffer) > buffer_size:
                    buffer.pop(0)
                i += 1
        Graypixels = np.array(buffer, dtype=np.uint8)
        RGBpixels = [gray2rgb(byte) for byte in Graypixels]
        [Gray_array_padded, RGB_array_padded] = paddArraystoMatrix(Graypixels, RGBpixels)
        if type(RGB_array_padded) is int:
            failedArray = PCAP_file_path
            return failedArray
        colour_image = Image.fromarray(RGB_array_padded, 'RGB')
        gray_image = Image.fromarray(Gray_array_padded)
        colour_image.save(IMAGE_OUTPUT_FINAL + PCAP_Name + str(i + 1) + colour_suffix)
        gray_image.save(IMAGE_OUTPUT_FINAL + PCAP_Name + str(i + 1) + gray_suffix)
    return PCAP_Name



