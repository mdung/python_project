import pandas as pd
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error, r2_score

# Generate synthetic student performance data
np.random.seed(42)
num_students = 1000

data = {
    'StudyHours': np.random.uniform(1, 10, num_students),
    'Attendance': np.random.uniform(0, 1, num_students),
    'PreviousGrades': np.random.uniform(0, 100, num_students),
    'FinalGrade': 0.3*np.random.uniform(1, 10, num_students) +
                  0.2*np.random.uniform(0, 1, num_students) +
                  0.5*np.random.uniform(0, 100, num_students) +
                  10*np.random.normal(size=num_students)
}

df = pd.DataFrame(data)

# Split the data into features (X) and target variable (y)
X = df[['StudyHours', 'Attendance', 'PreviousGrades']]
y = df['FinalGrade']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Standardize the features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Build the neural network model
model = Sequential()
model.add(Dense(16, activation='relu', input_dim=3))
model.add(Dense(8, activation='relu'))
model.add(Dense(1, activation='linear'))

# Compile the model
model.compile(optimizer='adam', loss='mean_squared_error', metrics=['mae'])

# Train the model
model.fit(X_train_scaled, y_train, epochs=50, batch_size=32, validation_split=0.2, verbose=2)

# Evaluate the model on the test set
y_pred = model.predict(X_test_scaled)

# Calculate metrics
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print(f'Mean Squared Error: {mse:.2f}')
print(f'R2 Score: {r2:.2f}')

# Example usage: Predict final grade for a new student
new_student_data = np.array([[7, 0.8, 85]])  # StudyHours, Attendance, PreviousGrades
new_student_data_scaled = scaler.transform(new_student_data)
predicted_final_grade = model.predict(new_student_data_scaled)[0][0]

print(f'Predicted Final Grade for the new student: {predicted_final_grade:.2f}')
