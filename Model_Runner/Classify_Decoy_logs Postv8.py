
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 16 18:14:14 2023

@author: callu
"""

import os
import cv2
import numpy as np
import PySimpleGUI as sg
from PIL import Image
from tensorflow import keras
from UserSetUp import *
import time
import io
import pprint
import random
import dpkt


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

def PCAP2_Image(PCAP_file_path, PCAP_Name):
    grayArray = []
    rgbArray = []
    buffer = []
    i = 0
    with open(PCAP_file_path, 'rb') as fp:
        for byte_s in fp:
            for byte in byte_s:
                byte = byte + 1
                if byte > 255: 
                    byte = 255;
                buffer += [byte]  # Add 1 to each new byte and append to the end of the buffer
                if len(buffer) > (150*150):
                    buffer.pop(0)
                if i % 200000 == 0:
                    Graypixels = np.array(buffer, dtype=np.uint8)
                    RGBpixels = [gray2rgb(byte) for byte in Graypixels]
                    [Gray_array_padded, RGB_array_padded] = paddArraystoMatrix(Graypixels, RGBpixels)
                    if type(RGB_array_padded) is int:
                        failedArray = PCAP_file_path
                        return failedArray
                    colour_image = Image.fromarray(RGB_array_padded, 'RGB')
                    gray_image = Image.fromarray(Gray_array_padded)
                    grayArray.append(gray_image) 
                    rgbArray.append(colour_image)
                i += 1
        # Save the final image
        if i > 0:
            Graypixels = np.array(buffer, dtype=np.uint8)
            RGBpixels = [gray2rgb(byte) for byte in Graypixels]
            [Gray_array_padded, RGB_array_padded] = paddArraystoMatrix(Graypixels, RGBpixels)
            if type(RGB_array_padded) is int:
                failedArray = PCAP_file_path
                return failedArray
            colour_image = Image.fromarray(RGB_array_padded, 'RGB')
            gray_image = Image.fromarray(Gray_array_padded)
            grayArray.append(gray_image) 
            rgbArray.append(colour_image)
        return rgbArray, grayArray




def num2cat(i,decoy):
  if Filetype == 0:
      if i == 0:
        return 'Botnet'
      elif i == 1:
        return 'Expanse'
      elif i == 2:
        return 'Exploitation'
      elif i == 4:
        return 'Censys-Inspect'
      return 'Other'
  elif  Filetype == 1:
    if i == 0:
        return 'DOS'
    elif i == 1:
        return 'Ladder'
    return 'Other'
  elif  Filetype == 2:
    if i == 0:
        return 'Command Injection'
    elif i == 2:
        return 'SQL Injection'
    return 'Other'


def show_Image(window, image, key):
    image = image.resize((window[key].Widget.winfo_width(), window[key].Widget.winfo_height())) # setting the size to display on the GUI
    bio = io.BytesIO()
    image.save(bio, format="PNG")
    window[key].update(data=bio.getvalue())


def jsonFile(filename):
    category = None
    total_add = 0
    correct = 0
    colour_img = "" 
    snippet = None
    mean_pred_Many = None  
    label = None 
    for cat in decoyCategories:
        if cat.lower() in root.lower():
            category = cat
            break 
    if category is None:
        category = 'Other'
        label = 3
    else:
        label = decoyCategories[category]
    json_path = os.path.join(root, filename)
    json_Name = os.path.splitext(json_path)[0]
    with open(json_path, 'r') as f:
        json_content = f.read()
    snippet = json_content[:1000] + '...'
    colour_img, gray_img = JSON2_Image(json_path,json_Name)
    imageNotFound = type(colour_img) == str
    if not imageNotFound:
        total_add = 1
        print(colour_img)
        gray_prediction_Many =predict_image(gray_img, Decoymodel)
        gray_predicted_label_Many = np.argmax(gray_prediction_Many)
        colour_prediction_Many =predict_image(colour_img, Decoymodel)
        colour_predicted_label_Many = np.argmax(colour_prediction_Many)
        mean_pred_Many = np.mean([gray_prediction_Many, colour_prediction_Many], axis=0)
        correct = np.argmax(mean_pred_Many) == label
        print(f'prediction: {np.argmax(mean_pred_Many)}')
        print(f'Actual Label: {label}')
        print(f'Root folder: {root}')
        print('\n')
    return imageNotFound, correct, colour_img, snippet, mean_pred_Many, label, total_add

def plcFile(filename):
    category = None
    total_add = 0
    correct = 0
    colour_img_array = []
    snippet = None
    mean_pred_Many = None  
    label = None 
    for cat in PLCCategories:
        if cat.lower() in root.lower():
            category = cat
            break 
    if category is None:
        category = 'Other'
        label = 2
    else:
        label = PLCCategories[category]
    pcap_path = os.path.join(root, filename)
    pcap_Name = os.path.splitext(pcap_path)[0]
    with open(pcap_path, 'rb') as f:
        pcap_content = f.read()
    snippet = str(pcap_content[:100]) + '...'
    colour_img_array, gray_img_array = PCAP2_Image(pcap_path,pcap_Name)
    imageNotFound = type(colour_img_array) == str
    if not imageNotFound:
        total_add = 1
        gray_prediction_Many = np.mean([predict_image(img, PLCmodel) for i, img in enumerate(gray_img_array) if i % 1 == 0], axis=0)
        gray_predicted_label_Many = np.argmax(gray_prediction_Many)
        colour_prediction_Many = np.mean([predict_image(img, PLCmodel) for i, img in enumerate(colour_img_array) if i % 1 == 0], axis=0)
        colour_predicted_label_Many = np.argmax(colour_prediction_Many)
        mean_pred_Many = np.mean([gray_prediction_Many, colour_prediction_Many], axis=0)
        correct = np.argmax(mean_pred_Many) == label
        # Calculate the mean prediction for all images
        print(f'prediction: {np.argmax(mean_pred_Many)}')
        print(f'Actual Label: {label}')
        print(f'Root folder: {root}')
        print('\n')
    return imageNotFound, correct, colour_img_array, snippet, mean_pred_Many, label, total_add

def dvwaFile(filename):
    category = None
    total_add = 0
    correct = 0
    colour_img_array = []
    snippet = None
    mean_pred_Many = None  
    label = None 
    for cat in DVWACategories:
        if cat.lower() in root.lower():
            category = cat
            break 
    if category is None:
        category = 'Other'
        label = 1
    else:
        label = DVWACategories[category]
    pcap_path = os.path.join(root, filename)
    pcap_Name = os.path.splitext(pcap_path)[0]
    with open(pcap_path, 'rb') as f:
        pcap_content = f.read()
    snippet = str(pcap_content[:100]) + '...'
    colour_img_array, gray_img_array = PCAP2_Image(pcap_path,pcap_Name)
    imageNotFound = type(colour_img_array) == str
    if not imageNotFound:
        total_add = 1
        gray_prediction_Many = np.mean([predict_image(img, DVWAmodel) for i, img in enumerate(gray_img_array) if i % 5 == 0], axis=0)
        gray_predicted_label_Many = np.argmax(gray_prediction_Many)
        colour_prediction_Many = np.mean([predict_image(img, DVWAmodel) for i, img in enumerate(colour_img_array) if i % 5 == 0], axis=0)
        colour_predicted_label_Many = np.argmax(colour_prediction_Many)
        mean_pred_Many = np.mean([gray_prediction_Many, colour_prediction_Many], axis=0)
        correct = np.argmax(mean_pred_Many) == label
        # Calculate the mean prediction for all images
        print(f'prediction: {np.argmax(mean_pred_Many)}')
        print(f'Actual Label: {label}')
        print(f'Root folder: {root}')
        print('\n')
    return imageNotFound, correct, colour_img_array, snippet, mean_pred_Many, label, total_add




def updateGUI(window, colour_img, filename, snippet, label, mean_pred_Many, correcount, total, Filetype):
    window['-FILENAME-'].update(filename)
    window['-SNIPPET-'].update(snippet)
    window['-SNIPPET-'].Widget.configure(highlightcolor=category_colors[num2cat(label, Filetype)], highlightthickness=8)
    if window['-RADIO-'].get():
        time.sleep(0.2)
        window.refresh()
    window['-ATTACK-'].update(num2cat(label, Filetype), background_color=category_colors[num2cat(label, Filetype)])
    if window['-RADIO-'].get():
        time.sleep(0.2)
        window.refresh()
    if type(colour_img) == list:
        for img in colour_img:
            show_Image(window, img, '-IMAGE-')
            time.sleep(0.5)
            window.refresh()
    else:
        show_Image(window, colour_img, '-IMAGE-')
    if window['-RADIO-'].get():
        time.sleep(0.2)
        window.refresh()
    window['-COLOR-'].update('', background_color=category_colors[num2cat(np.argmax(mean_pred_Many), Filetype)])
    window['-PREDICTION-'].update(num2cat(np.argmax(mean_pred_Many), Filetype), background_color=category_colors[num2cat(np.argmax(mean_pred_Many), Filetype)])
    window.refresh()
    if window['-RADIO-'].get():
        time.sleep(0.2)
        window.refresh()
    if correct:
        window['-CORRECT-'].update('True', background_color='green')
    else:
        window['-CORRECT-'].update('False', background_color='red')
    window['-PROGRESSBAR-'].update_bar((correcount/total) * 1000)
    window['-PERCENT-'].update(f'{int((correcount/total) * 100)}%  of {total} files')
    window.refresh()
    time.sleep(1.5)

def clearGUI(window):
    window['-FILENAME-'].update('')
    window['-SNIPPET-'].update('Snippet of file...')
    window['-SNIPPET-'].Widget.configure(highlightcolor='White', highlightthickness=0)
    window['-ATTACK-'].update('')
    window['-ATTACK-'].Widget.configure(background='white',width=13, height=1)
    window['-IMAGE-'].update(filename='', data=None)
    window['-IMAGE-'].Widget.configure(width=300, height=300)
    window['-COLOR-'].update('Bytes as Image')
    window['-COLOR-'].Widget.configure(width=45, height=2, background='white')
    window['-PREDICTION-'].update('')
    window['-PREDICTION-'].Widget.configure(background='white',width=13, height=1)
    window['-CORRECT-'].update('')
    window['-CORRECT-'].Widget.configure(background='white',width=4, height=1)


# Load the pre-trained model
Decoymodel = keras.models.load_model('keras_saved_model_Decoy')
PLCmodel = keras.models.load_model('keras_saved_model_PLC')
DVWAmodel = keras.models.load_model('keras_saved_model_Injection')
# Define the categories and their corresponding labels
decoyCategories = {
    'Botnet': 0,
    'Expanse': 1,
    'Exploitation': 2,
    'Censys-Inspect': 4
}

PLCCategories = {
    'DOS': 0,
    'Ladder': 1,
}

DVWACategories ={
    'comsi':0,
    'sqli': 2,
    }
  
category_colors = {
    'Botnet': 'orange',
    'Expanse': 'mediumblue',
    'Exploitation': 'orchid',
    'Other': 'gold',
    'Censys-Inspect': 'teal',
    'Ladder': 'crimson',
    'DOS': 'slateblue',
    'Command Injection': 'darkred',
    'SQL Injection': 'indianred'
}

path ='Example_DecoySet/'

# Define the PySimpleGUI layout
layout = [    [sg.Image(source='TitleImage4.png', key='-TITLE-', size=(1000, 100))],
    [sg.Column(layout=[[sg.Image(key='-IMAGE-', size=(250, 250), pad=((5, 5), 0))],
        [sg.Text('Bytes as Image', size=(45, 2), key='-COLOR-', background_color='White', text_color='black')],
    ], element_justification='center', pad=((10, 10), 20)),
    sg.Column(layout=[
        [sg.Multiline(default_text='Snippet of File...', size=(75, 15), key='-SNIPPET-')],
        [sg.Input(size=(35, 1), key="-FOLDER-"), sg.FolderBrowse(initial_folder=path), sg.Button("Classify")],
        [sg.Radio('Wait', "RADIO1", default=False, key='-RADIO-'), sg.Radio('Do not Wait', "RADIO1", default=True)],
        [sg.Text('Accuracy Bar: '), sg.ProgressBar(1000, orientation='horizontal', size=(25, 25), key='-PROGRESSBAR-', bar_color=('green', 'red')), sg.Text(key='-PERCENT-', font=('Helvetica', 12))],
    ], element_justification='center', pad=((20, 20), (20, 40))),
    ],
    [sg.Text('File: '), sg.Text(key='-FILENAME-', font=('Helvetica', 12))],
    [sg.Text('Prediction: '), sg.Text(key='-PREDICTION-', font=('Helvetica', 12), size=(13, 1))],
    [sg.Text('Attack Type: '), sg.Text(key='-ATTACK-', font=('Helvetica', 12), size=(13, 1))],
    [sg.Text('Correct: '), sg.Text(key='-CORRECT-', font=('Helvetica', 12), size=(4, 1))],
]

#, size=(15,2)


# Create the window
window = sg.Window('Classifier', layout, icon='Icon1.ico')
# Create the window




while True:
    event, values = window.read()
    clearGUI(window)
    if event == "Exit" or event == sg.WIN_CLOSED:
        window.close()
        break
    if event == "Classify": 
        foldername = values["-FOLDER-"]
        if os.path.exists(foldername):
            path = foldername
        correcount = 0
        total = 0
        Filetype = 0
        for root, dirs, files in os.walk(path):
            for filename in files:
                clearGUI(window)
                window.refresh()
                total_add = 0
                if 'Decoy' in root:
                    Filetype = 0
                    if filename.endswith('.json'):
                        imageNotFound, correct, colour_img, snippet, mean_pred_Many, label, total_add = jsonFile(filename)
                elif 'PLC' in root:
                     Filetype = 1
                     window['-SNIPPET-'].update("PCAP FILE FOUND \n     Simulating Packet Capture through PCAP Breakdown")
                     window.refresh()
                     imageNotFound, correct, colour_img, snippet, mean_pred_Many, label, total_add = plcFile(filename)
                elif 'DVWA' in root:
                    Filetype = 2
                    window['-SNIPPET-'].update("PCAP FILE FOUND \n     Simulating Packet Capture through PCAP Breakdown")
                    window.refresh()
                    imageNotFound, correct, colour_img, snippet, mean_pred_Many, label, total_add = dvwaFile(filename)
                total = total + total_add
                if not imageNotFound:
                    if correct:
                        correcount += int(correct)
                    updateGUI(window,colour_img,filename, snippet, label, mean_pred_Many,correcount, total, Filetype)
                window.refresh()

window.close()

