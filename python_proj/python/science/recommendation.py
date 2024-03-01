import pandas as pd
from surprise import Dataset, Reader, SVD
from surprise.model_selection import train_test_split
from surprise.accuracy import rmse
from collections import defaultdict

# Load the MovieLens dataset (you can replace this with your own dataset)
data = Dataset.load_builtin('ml-100k')

# Split the dataset into training and testing sets
trainset, testset = train_test_split(data, test_size=0.25)

# Choose the Singular Value Decomposition (SVD) algorithm
algorithm = SVD()

# Train the model on the training set
algorithm.fit(trainset)

# Make predictions on the testing set
predictions = algorithm.test(testset)

# Evaluate the model's performance
print("RMSE on test set:", rmse(predictions))

# Get top N movie recommendations for a user
def get_top_n_recommendations(predictions, n=10):
    top_n = defaultdict(list)
    for uid, iid, true_r, est, _ in predictions:
        top_n[uid].append((iid, est))

    # Sort the predictions for each user and retrieve the top N
    for uid, user_ratings in top_n.items():
        user_ratings.sort(key=lambda x: x[1], reverse=True)
        top_n[uid] = user_ratings[:n]

    return top_n

# Get top N recommendations for a specific user
user_id = str(196)  # Replace with a user ID from the dataset
user_movies = get_top_n_recommendations(predictions)[user_id]

# Display the top N movie recommendations for the user
print(f"\nTop 5 movie recommendations for User {user_id}:")
for movie_id, estimated_rating in user_movies:
    print(f"Movie ID: {movie_id}, Estimated Rating: {estimated_rating}")
