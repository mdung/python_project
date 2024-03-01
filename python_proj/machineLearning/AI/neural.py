import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# Create a sample dataset
# Assume we have a dataset with user preferences (features) and labels indicating preferences (0 or 1)
data = {
    'Feature1': np.random.rand(1000),
    'Feature2': np.random.rand(1000),
    'Preference': np.random.randint(2, size=1000)
}

df = pd.DataFrame(data)

# Split the dataset into features (X) and labels (y)
X = df[['Feature1', 'Feature2']].values
y = df['Preference'].values

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Standardize the features
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Build a neural network model
model = Sequential()
model.add(Dense(32, input_dim=2, activation='relu'))
model.add(Dense(16, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

# Compile the model
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Train the model
model.fit(X_train, y_train, epochs=10, batch_size=32, validation_split=0.2)

# Evaluate the model on the test set
y_pred = model.predict(X_test)
y_pred_binary = np.round(y_pred).flatten()

accuracy = accuracy_score(y_test, y_pred_binary)
print(f"Accuracy on the test set: {accuracy}")
