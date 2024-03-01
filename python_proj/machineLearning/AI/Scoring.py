import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn import preprocessing

# Load or create a dataset (you would replace this with your actual credit scoring dataset)
# For demonstration, let's create a simple example dataset
data = {
    'Age': [25, 35, 45, 22, 50, 60, 30, 40],
    'Income': [50000, 80000, 120000, 30000, 150000, 100000, 70000, 90000],
    'Credit_Score': [600, 700, 800, 500, 850, 750, 650, 720],
    'Approved': [0, 1, 1, 0, 1, 1, 0, 1]  # 1 indicates approval, 0 indicates rejection
}

df = pd.DataFrame(data)

# Separate features (X) and target variable (y)
X = df[['Age', 'Income', 'Credit_Score']]
y = df['Approved']

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Standardize the features (optional, but can be beneficial for decision trees)
scaler = preprocessing.StandardScaler().fit(X_train)
X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)

# Build a decision tree model
model = DecisionTreeClassifier(random_state=42)

# Train the model
model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred)

print(f"Accuracy: {accuracy}")
print("Classification Report:\n", report)
