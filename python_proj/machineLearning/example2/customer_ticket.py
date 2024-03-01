import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.svm import SVC
from sklearn.metrics import classification_report, accuracy_score

# Sample customer support ticket data (replace with your actual data)
data = {
    'text': [
        'My internet is not working.',
        'I cannot log in to my account.',
        'I want to cancel my subscription.',
        'My order was not delivered on time.',
        'The product is defective.'
    ],
    'category': ['Internet', 'Login', 'Cancellation', 'Delivery', 'Product']
}

# Create a DataFrame from the data
df = pd.DataFrame(data)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(df['text'], df['category'], test_size=0.2, random_state=42)

# Convert text data to a bag-of-words representation
vectorizer = CountVectorizer()
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

# Train a Support Vector Machine (SVM) classifier
clf = SVC(kernel='linear')
clf.fit(X_train_vec, y_train)

# Make predictions on the test data
predictions = clf.predict(X_test_vec)

# Evaluate the classifier
accuracy = accuracy_score(y_test, predictions)
classification_rep = classification_report(y_test, predictions)

print(f"Accuracy: {accuracy}")
print("Classification Report:\n", classification_rep)
