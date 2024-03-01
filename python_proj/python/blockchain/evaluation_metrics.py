import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# Load your blockchain transaction data (replace 'your_dataset.csv' with the actual file name)
data = pd.read_csv('your_dataset.csv')

# Explore your data and perform necessary preprocessing
# For simplicity, let's assume 'label' is the target variable indicating normal or suspicious transactions
# You may need to adjust the features based on your dataset

# Drop unnecessary columns
data = data.drop(['unnecessary_column1', 'unnecessary_column2'], axis=1)

# Handle missing values if any
data = data.dropna()

# Convert categorical variables to numerical using one-hot encoding
data = pd.get_dummies(data, columns=['categorical_feature1', 'categorical_feature2'])

# Split the data into features (X) and target variable (y)
X = data.drop('label', axis=1)
y = data['label']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize a Random Forest classifier (you can use other algorithms as well)
clf = RandomForestClassifier(n_estimators=100, random_state=42)

# Train the classifier
clf.fit(X_train, y_train)

# Make predictions on the test set
y_pred = clf.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy:.2f}')

# Display classification report
print('\nClassification Report:')
print(classification_report(y_test, y_pred))
