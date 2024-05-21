import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')
import os
import pickle

for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))

patients = pd.read_csv('indian_liver_patient.csv')
patients['Gender'] = patients['Gender'].apply(lambda x: 1 if x == 'Male' else 0)

from sklearn.model_selection import train_test_split

X = patients[['Age', 'Gender', 'Total_Bilirubin', 'Direct_Bilirubin',
              'Alkaline_Phosphotase', 'Alamine_Aminotransferase',
              'Aspartate_Aminotransferase', 'Total_Protiens', 'Albumin',
              'Albumin_and_Globulin_Ratio']]
y = patients['Dataset']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix

logmodel = LogisticRegression()
logmodel.fit(X_train, y_train)

# Saving the trained model as a pickle file
with open('logistic_regression_model.pkl', 'wb') as file:
    pickle.dump(logmodel, file)

# Loading the saved model from the pickle file
with open('logistic_regression_model.pkl', 'rb') as file:
    loaded_model = pickle.load(file)

# Using the loaded model to make predictions
input_data = np.array([[0, 0.7, 0.1, 187, 16, 18, 6.8, 3.3, 0.9]])  # Assuming the second element represents 'Male'
predicted_class = loaded_model.predict(input_data)

print("Predicted class:", predicted_class)
