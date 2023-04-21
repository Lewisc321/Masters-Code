import os
import time
import cv2
import numpy as np
import tkinter as tk
from tkinter import messagebox
from tensorflow import keras
import tensorflow as tf
# Load the pre-trained model
model = keras.models.load_model('keras_saved_model_9')

batch_size = 48
epochs = 20
test_dir = 'test/'


import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import classification_report, confusion_matrix



# Define the circular buffer of image names
image_names = ['image1.png', 'image2.png', 'image3.png', 'image4.png']
image_idx = 0
predictions = []

# Define the folder to monitor
folder_to_watch = 'C:/VM_Folder/pcapImageBuffer'

# Define the function to perform predictions on new images
def predict_image(image_path):
    img = cv2.imread(image_path)
    img = img.astype('float32') / 255  # Rescale the image
    img = np.expand_dims(img, axis=0)
    preds = model.predict(img)
    return preds

# Define the function to pop up a warning message
def show_warning(warning):
    root = tk.Tk()
    root.withdraw()
    messagebox.showwarning("Warning", warning)
latest_file = None 
# Start monitoring the folder
while True:
    time.sleep(0.1) # Check every second
    files = os.listdir(folder_to_watch)
    if len(files) > 0:
        timefiles = [os.path.join(folder_to_watch, f) for f in files if f.endswith('.png')]
        timefiles.sort(key=os.path.getmtime)
        new_file = os.path.basename(timefiles[-1]) # Get the newest file
        if new_file in image_names:
            if latest_file !=new_file:
                latest_file = new_file
                image_path = os.path.join(folder_to_watch, new_file)
                preds = predict_image(image_path)
                predictions.append(np.argmax(preds))
                print(predictions)
                if len(set(predictions)) == 1 and len(predictions) == 2:
                    if predictions[0]== 0:
                        print("Injection in Progress")
                        show_warning("Injection in Progress")
                    if predictions[0] == 2:
                        print("Cross Site Script in Progress")
                        show_warning("Cross Site Script in Progress")
                if len(predictions) == 3:
                   predictions =[]
                            
                            
                            
                            