import pandas as pd
from surprise import Dataset, Reader, SVD
from surprise.model_selection import train_test_split
from surprise import accuracy

# Sample online course recommendation data (replace with your actual data)
data = {
    'User': ['User1', 'User2', 'User3', 'User4', 'User5'],
    'Course': ['Course A', 'Course B', 'Course A', 'Course C', 'Course B'],
    'Rating': [4, 5, 3, 4, 2]
}

# Create a DataFrame from the data
df = pd.DataFrame(data)

# Load the data into the Surprise dataset format
reader = Reader(rating_scale=(1, 5))
dataset = Dataset.load_from_df(df[['User', 'Course', 'Rating']], reader)

# Split the dataset into training and testing sets
trainset, testset = train_test_split(dataset, test_size=0.2, random_state=42)

# Train a Singular Value Decomposition (SVD) collaborative filtering model
model = SVD()
model.fit(trainset)

# Make predictions on the test set
predictions = model.test(testset)

# Calculate RMSE (Root Mean Squared Error) for the predictions
rmse = accuracy.rmse(predictions)

# Generate recommendations for a specific user
user_id = 'User1'
items_to_recommend = df['Course'].unique()
already_rated = df[df['User'] == user_id]['Course']
items_to_recommend = [item for item in items_to_recommend if item not in already_rated]
user_predictions = [model.predict(user_id, item) for item in items_to_recommend]
recommended_items = sorted(user_predictions, key=lambda x: x.est, reverse=True)

print(f"Recommended courses for {user_id}:")
for prediction in recommended_items:
    print(f"{prediction.iid} (Estimated rating: {prediction.est:.2f})")
