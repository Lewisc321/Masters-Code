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
import io
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


def predict_image(img, model):
    img = np.array(img)
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


def num2cat(i,many):
  if many:
      if i == 0:
        return 'botnet'
      elif i == 1:
        return 'expanse'
      elif i == 2:
        return 'exploitation'
      elif i == 3:
        return 'censys-inspect'
      return 'Other'
  else:
    if i == 0:
        return 'botnet'
    elif i == 1:
        return 'exploitation'
    return 'other'


def show_Image(window, image, key):
    image.thumbnail((400, 400)) # setting the size to display on the GUI
    bio = io.BytesIO()
    image.save(bio, format="PNG")
    window[key].update(data=bio.getvalue()) # Updating the GUI window using the key that passed in


# Load the pre-trained model
modelMany = keras.models.load_model('keras_saved_model')
modelFew = keras.models.load_model('keras_saved_model_Decoy')
# Define the categories and their corresponding labels
categories = {
    'botnet': 0,
    'expanse': 1,
    'exploitation': 2,
    'censys-inspect': 4
}

# Define the PySimpleGUI layout
layout = [    [sg.Image(key='-IMAGE-'), sg.Multiline(default_text='', size=(50, 10), key='-SNIPPET-')],
    [sg.Text('File: '), sg.Text(key='-FILENAME-')],
    [sg.Text('Prediction: '), sg.Text(key='-PREDICTION-')],
    [sg.Text('Attack Type: '), sg.Text(key='-ATTACK-')],
    [sg.Text('Correct: '), sg.Text(key='-CORRECT-')],
    [sg.Text('Accuracy Bar: '), sg.ProgressBar(1000, orientation='horizontal', size=(20, 20), key='-PROGRESSBAR-', bar_color=('green', 'red'))],
    [sg.Button('Quit')]
]

# Create the window
window = sg.Window('Classifier', layout)

path ='DecoySet/'
# Create the PySimpleGUI window
# Walk through the directory and classify each image
correcount = 0
total = 0
for root, dirs, files in os.walk(path):
    for filename in files:
        event, values = window.read(timeout=10)
        if filename.endswith('.json'):
            category = None
            for cat in categories:
                if cat in root:
                    category = cat
                    break 
            if category is None:
                category = 'Other'
                label = 3
            else:
                label = categories[category]
            json_path = os.path.join(root, filename)
            json_Name = os.path.splitext(json_path)[0]
            with open(json_path, 'r') as f:
                json_content = f.read()
            snippet = json_content[:500] + '...'
            colour_img, gray_img = JSON2_Image(json_path,json_Name)
            if not type(colour_img) == str:
                total += 1
                print(colour_img)
                gray_prediction_Many =predict_image(gray_img, modelMany)
                gray_predicted_label_Many = np.argmax(gray_prediction_Many)
                colour_prediction_Many =predict_image(colour_img, modelMany)
                colour_predicted_label_Many = np.argmax(colour_prediction_Many)

                # gray_prediction_Few = predict_image(gray_img, modelFew)
                # gray_predicted_label_Few = np.argmax(gray_prediction_Few)
                # colour_prediction_Few = predict_image(colour_img, modelFew)
                # colour_predicted_label_Few = np.argmax(colour_prediction_Few)

                # mean_pred_Few = np.mean([gray_prediction_Few, colour_prediction_Few], axis=0)
                mean_pred_Many = np.mean([gray_prediction_Many, colour_prediction_Many], axis=0)

                correct = np.argmax(mean_pred_Many) == label
                if correct:
                    correcount += int(correct)
                show_Image(window, colour_img, '-IMAGE-')
                window['-FILENAME-'].update(filename)
                window['-PREDICTION-'].update(num2cat(np.argmax(mean_pred_Many), True))
                window['-ATTACK-'].update(num2cat(np.argmax(label), True))
                window['-SNIPPET-'].update(snippet)
                if correct:
                    window['-CORRECT-'].update('True', background_color='green')
                else:
                    window['-CORRECT-'].update('False', background_color='red')
                window['-PROGRESSBAR-'].update_bar((correcount/total) * 1000)
        window.refresh()
        if event == sg.WIN_CLOSED or event == 'Exit':
            break