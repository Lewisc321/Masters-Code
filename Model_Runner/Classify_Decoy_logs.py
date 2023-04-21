import os
import time
import numpy as np
import tkinter as tk
from tkinter import messagebox
from tensorflow import keras
import tensorflow as tf
from PIL import Image
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

# Load the pre-trained model
model = keras.models.load_model('keras_saved_model_Decoy')


# Define the function to perform predictions on new images
def predict_image(img):
    img = img.astype('float32') / 255
    img = np.expand_dims(img, axis=0)
    preds = model.predict(img)
    return preds

# Define the function to pop up a warning message
def show_warning(warning):
    root = tk.Tk()
    root.withdraw()
    messagebox.showwarning("Warning", warning)

# Define the folder to monitor
folder_to_watch = 'C:/VM_Folder/DecoyJSONBuffer'

# Define the circular buffer of JSON file names
#json_names = ['json1.json', 'json2.json', 'json3.json', 'json4.json']
json_idx = 0
predictions = []

# Start monitoring the folder
while True:
    time.sleep(0.1) # Check every second
    files = os.listdir(folder_to_watch)
    if len(files) > 0:
        timefiles = [os.path.join(folder_to_watch, f) for f in files if f.endswith('.json')]
        timefiles.sort(key=os.path.getmtime)
        new_file = os.path.basename(timefiles[-1]) # Get the newest file
        if '.json' in new_file:
            # Load the JSON file and convert it to images
            json_path = os.path.join(folder_to_watch, new_file)
            PCAP_Name = os.path.splitext(new_file)[0]
            colour_image, gray_image = JSON2_Image(json_path, PCAP_Name)
            
            # Pass the images through the model and make a prediction
            colour_img_arr = np.array(colour_image)
            gray_img_arr = np.array(gray_image)
            colour_img_arr = colour_img_arr  # Rescale the image
            gray_img_arr = gray_img_arr # Rescale the image
            colour_preds = predict_image(colour_img_arr)
            #gray_preds = predict_image(gray_img_arr)
            preds = colour_preds
            pred_class = np.argmax(preds)
            predictions.append(pred_class)
            
            # Raise a warning if the predicted class is 0 or 1
            if len(set(predictions)) == 1 and len(predictions) == 2:
                if predictions[0] == 0:
                    print("Botnet Detected")
                    show_warning("Botnet Detected")
                elif predictions[0] == 1:
                    print("Exploitation Detected")
                    show_warning("Exploitation in Progress")
                
            # Reset the prediction buffer after 3 predictions
            if len(predictions) == 2:
                predictions = []
