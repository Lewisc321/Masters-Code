"""""

@author=Lewis 

Decision Tree Classifier


"""

#Import Libraries
import pandas as pd
from pandas import DataFrame, Series
import sklearn as sk
import numpy as np
import joblib
import collections
from IPython.display import Image

#Point to Directory
csv_path = '/Users/lewis/Desktop/Uni/5th_Year/EM501/PYTHON_Code/DecisionTree/'

#Point to File
df = pd.read_csv(csv_path + 'Training_Data_2.csv', low_memory=False)

#%Decision Tree Imports
from sklearn import tree
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier, export_graphviz
from sklearn.model_selection import train_test_split

#Define Target and Inputs
target = df['Attack_type']

inputs = df.drop(['Attack_type'], axis='columns')
inputs = inputs.drop(['Log'], axis='columns')

#Define Train Test Split
X_train, X_test, y_train, y_test = train_test_split(inputs, target, test_size=0.3, random_state=1)

#Decision Tree Testing
model = tree.DecisionTreeClassifier(max_depth=5)
model = model.fit(X_train,y_train)

# Save the trained model
filename = 'trained_model.joblib'
joblib.dump(model, filename)

#Export the decision tree to a file
tree.plot_tree(model)

tree.export_graphviz(model,
                    out_file="model.dot",
                    feature_names=inputs.columns)

#Accuracy Score
from sklearn.metrics import accuracy_score
y_pred = model.predict(X_test)
print(accuracy_score(y_test,y_pred))

# Classification Report
from sklearn.metrics import classification_report
print(classification_report(y_test,y_pred))

# Confusion Matirx
from sklearn.metrics import confusion_matrix
y_pred = model.predict(X_test)
print(confusion_matrix(y_test,y_pred))