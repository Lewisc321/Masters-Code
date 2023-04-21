# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 11:28:30 2023

@author: callu
"""

import os
import cv2
import numpy as np
import PySimpleGUI as sg
from PIL import Image
from tensorflow import keras
from UserSetUp import *

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


def predict_image(img):
    if img.ndim == 2:
        # Grayscale image
        img = np.stack((img,) * 3, axis=-1)  # Convert to RGB by repeating channels
    elif img.ndim == 3 and img.shape[-1] == 3:
        # RGB image
        pass
    else:
        raise ValueError("Input image must be grayscale or RGB")

    img = img.astype('float32') / 255
    img = np.expand_dims(img, axis=0)
    preds = model.predict(img)
    return preds



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


# Load the pre-trained model
model = keras.models.load_model('keras_saved_model_9')

# Define the categories and their corresponding labels
categories = {
    'botnet': 0,
    'exploitation': 1,
    'other': 2
}



# # Define the PySimpleGUI layout
# layout = [
#     [sg.Image(key='-IMAGE-')],
#     [sg.Text('File: '), sg.Text(key='-FILENAME-')],
#     [sg.Text('Prediction: '), sg.Text(key='-PREDICTION-')],
#     [sg.Text('Correct: '), sg.Text(key='-CORRECT-')],
#     [sg.Button('Quit')]
# ]

# # Create the window
# window = sg.Window('Classifier', layout)

path ='C:/Users/callu/Documents/Python Scripts/Building/DecoyLogDeconstruct/DecoySet/'
# Create the PySimpleGUI window
# Walk through the directory and classify each image
for root, dirs, files in os.walk(path):
    for filename in files:
        print('here')
        if filename.endswith('.json'):
            print(filename)
            category = None
            for cat in categories:
                if cat in root:
                    category = cat
                    break
            if category is None:
                label = 2
            else:
                label = categories[category]
            print(category)
            json_path = os.path.join(root, filename)
            json_Name = os.path.splitext(json_path)[0]
            color_img, gray_img = JSON2_Image(json_path,json_Name)
            if not type(color_img) == str:
                print(color_img)
                img_array = np.array(color_img)
                prediction =predict_image(img_array)
                predicted_label = np.argmax(prediction)
                if predicted_label != 0:
                    print('Hooray!!!!')
                    break;
                print(predicted_label)
                print(label)
                correct = predicted_label == label
                print(correct)
            print('\n')
            
#             window['-IMAGE-'].update(data=color_img.tobytes())
#             window['-FILENAME-'].update(filename)
#             window['-PREDICTION-'].update(str(predicted_label))
#             if correct:
#                 window['-CORRECT-'].update('True', background_color='green')
#             else:
#                 window['-CORRECT-'].update('False', background_color='red')
#             window.refresh()
#     event, values = window.read()
#     if event == sg.WIN_CLOSED or event == 'Quit':
#         break



# window.close()
