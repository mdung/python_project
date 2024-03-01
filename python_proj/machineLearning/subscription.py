import features as features
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Load your dataset (replace 'data.csv' with your actual dataset)
data = pd.read_csv('data.csv')
print(data.columns)

# Verify the value of the 'features' variable
print(features)

# Access a specific column using its name to test
print(data['churn'])
# Assume 'features' are the columns you want to use for prediction, and 'target' is the churn column
features = ['feature1', 'feature2', 'feature3', 'churn']
target = 'churn'

# Split data into features (X) and target (y)
X = data[features]
y = data[target]

# Convert categorical features to numerical using LabelEncoder (if needed)
label_encoders = {}
for col in X.select_dtypes(include=['object']).columns:
    le = LabelEncoder()
    X[col] = le.fit_transform(X[col])
    label_encoders[col] = le

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a decision tree classifier
model = DecisionTreeClassifier(random_state=42)

# Train the model
model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
confusion = confusion_matrix(y_test, y_pred)
classification_rep = classification_report(y_test, y_pred)

print("Accuracy:", accuracy)
print("Confusion Matrix:\n", confusion)
print("Classification Report:\n", classification_rep)

# You can use the trained model to make predictions for new data
new_data = pd.DataFrame({
    'feature1': [value1],
    'feature2': [value2],
    'feature3': [value3],
    # ...
})

# Convert categorical features to numerical using the saved LabelEncoders
for col, le in label_encoders.items():
    new_data[col] = le.transform(new_data[col])

new_prediction = model.predict(new_data)

if new_prediction[0] == 0:
    print("Customer is not likely to churn.")
else:
    print("Customer is likely to churn.")
