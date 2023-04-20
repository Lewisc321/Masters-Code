"""""

@author=Lewis 

Decision Tree Classifier


"""

import joblib
import pandas as pd

# Load the trained model
filename = 'trained_model.joblib'
loaded_model = joblib.load(filename)

# Load new data for prediction (replace 'new_data.csv' with your new data file)
new_data = pd.read_csv('new_data.csv')

# Make predictions
predictions = loaded_model.predict(new_data)

# Print predictions
print(predictions)
