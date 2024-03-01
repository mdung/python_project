import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
import joblib
import os

# Load data
data_dir = os.path.join(os.path.dirname(__file__), '..', 'data')
data = pd.read_csv(os.path.join(data_dir, 'usage_data.csv'))

# Feature engineering
features = data[['cpu_usage', 'ram_usage', 'storage_usage', 'transaction_count']]
target = data['recommended_resource']

# Split data
X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)

# Train the model
model = DecisionTreeClassifier()
model.fit(X_train, y_train)

# Save the model
models_dir = os.path.join(os.path.dirname(__file__), '..', 'models')
os.makedirs(models_dir, exist_ok=True)
model_filename = os.path.join(models_dir, 'decision_tree_model.pkl')

joblib.dump(model, model_filename)
print(f"Model saved to {model_filename}")
