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


RGBpixels = []
Graypixels =[]

def extendbyte(start, end,bi):
     return int((int(bi[start:end],2)/8) * 2**8)

def gray2rgb(byte):
     bi = format(byte+1,'08b').replace("0b", "")
     r = extendbyte(0,3,bi)
     g = extendbyte(2,5,bi)
     b = extendbyte(7,8,bi)
     return([r,g,b])

def createArray(fileName):
    Graypixels =[]
    RGBpixels =[]
    with open(fileName, 'rb') as fp:
        while 1:  
            byte_s = fp.read(1)
            if not byte_s:
                break;
            byte = byte_s[0]
            Graypixels.append(byte+1)        
            RGBpixels.append(gray2rgb(byte))
    return(Graypixels, RGBpixels)

def paddArraystoMatrix(gray, colour):
    rgb_padded =[]
    gray_padded = []
    if len(gray)<max_Pixels:
        padding = max_Pixels-len(gray)
        gray.extend(np.zeros(padding))
        for _ in range(padding):
            colour.append([0,0,0])
    rgb_padded = np.array(colour, dtype=np.uint8).reshape((pixelDimen, pixelDimen, 3))
    gray_padded = np.array(gray, dtype=np.uint8).reshape((pixelDimen, pixelDimen))
    return (gray_padded, rgb_padded)
#

def PCAP2_Image(PCAP_file_path, PCAP_Name):
    Gray_array = []
    RGB_array =[]
    Gray_array_padded=[]
    RGB_array_padded =[]

    [Gray_array, RGB_array] = createArray(PCAP_file_path)
    [Gray_array_padded, RGB_array_padded] = paddArraystoMatrix(Gray_array,RGB_array)
    colour_image = Image.fromarray(RGB_array_padded, 'RGB')
    colour_image.save(IMAGE_OUTPUT + PCAP_Name + colour_suffix)
    gray_image = Image.fromarray(Gray_array_padded)
    gray_image.save(IMAGE_OUTPUT + PCAP_Name +  gray_suffix)



PCAP2_Image('./Example_PCAPS/XSSSTOREDTTACKS\9_CM_xss_stored_hard_p.pcap', '9_CM_xss_stored_hard_p')
PCAP2_Image('./Example_PCAPS/XSSSTOREDTTACKS\9_CM_xss_stored_hard_p.pcap', '9_CM_xss_stored_hard_p')
PCAP2_Image('./Example_PCAPS/XSSSTOREDTTACKS\9_CM_xss_stored_hard_p.pcap', '9_CM_xss_stored_hard_p')







