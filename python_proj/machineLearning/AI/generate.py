import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import LabelEncoder
from sklearn.pipeline import Pipeline

# Load the dataset (replace 'weather_data.csv' with your dataset)
data = pd.read_csv('weather_data.csv')

# Drop unnecessary columns for simplicity
data = data.drop(['Date', 'Location', 'RISK_MM'], axis=1)

# Convert 'RainTomorrow' column to binary labels
data['RainTomorrow'] = LabelEncoder().fit_transform(data['RainTomorrow'])

# Split the data into features (X) and target variable (y)
X = data.drop('RainTomorrow', axis=1)
y = data['RainTomorrow']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Define a preprocessing pipeline with imputation and a random forest classifier
model_pipeline = Pipeline([
    ('imputer', SimpleImputer(strategy='mean')),
    ('classifier', RandomForestClassifier(n_estimators=100, random_state=42))
])

# Train the model
model_pipeline.fit(X_train, y_train)

# Make predictions on the test set
y_pred = model_pipeline.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy:.2f}\n')

print('Classification Report:')
print(classification_report(y_test, y_pred))

# Example usage: Predict weather for a new set of features
new_data = pd.DataFrame({
    'MinTemp': [20],
    'MaxTemp': [30],
    'Rainfall': [0],
    'WindGustSpeed': [25],
    'WindSpeed9am': [15],
    'Humidity9am': [70],
    'Humidity3pm': [50],
    'Pressure9am': [1015],
    'Pressure3pm': [1010],
    'Temp9am': [25],
    'Temp3pm': [28],
    'WindDir9am': ['N'],
    'WindDir3pm': ['W']
})

# Preprocess and predict
new_prediction = model_pipeline.predict(new_data)
print(f'Predicted weather tomorrow: {"Yes" if new_prediction[0] == 1 else "No"}')
