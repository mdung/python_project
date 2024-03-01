import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics.pairwise import cosine_similarity

class MovieRecommendationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Movie Recommendation System")

        # Create Frame
        self.frame = tk.Frame(root)
        self.frame.pack(padx=10, pady=10)

        # Add Buttons
        self.load_data_button = tk.Button(self.frame, text="Load Movie Data", command=self.load_data)
        self.load_data_button.pack(pady=10)

        self.recommend_button = tk.Button(self.frame, text="Get Movie Recommendations", command=self.get_recommendations)
        self.recommend_button.pack(pady=10)

        # Initialize DataFrame
        self.movie_data = pd.DataFrame()
        self.user_preferences = {}

    def load_data(self):
        file_path = filedialog.askopenfilename(title="Select MovieLens Dataset CSV file",
                                               filetypes=[("CSV Files", "*.csv")])
        if file_path:
            self.movie_data = pd.read_csv(file_path)
            tk.messagebox.showinfo("Success", "Movie data loaded successfully!")

    def get_recommendations(self):
        if self.movie_data.empty:
            tk.messagebox.showwarning("Warning", "Please load movie data first.")
            return

        # Get user preferences (example: MovieID and rating)
        user_preferences_input = tk.simpledialog.askstring("User Preferences",
                                                           "Enter your movie preferences (MovieID:Rating, separated by comma):")
        if not user_preferences_input:
            tk.messagebox.showwarning("Warning", "Please enter your movie preferences.")
            return

        # Convert user input to a dictionary
        try:
            user_preferences_list = [preference.split(":") for preference in user_preferences_input.split(",")]
            self.user_preferences = {int(movie_id): float(rating) for movie_id, rating in user_preferences_list}
        except ValueError:
            tk.messagebox.showwarning("Warning", "Invalid input format. Please use MovieID:Rating format.")
            return

        # Preprocess data and build a recommendation model
        movie_ratings = self.movie_data.pivot_table(index='userId', columns='title', values='rating')
        movie_ratings = movie_ratings.fillna(0)

        # Add user preferences to the dataset
        for movie_id, rating in self.user_preferences.items():
            movie_ratings.loc[0, movie_id] = rating

        # Calculate cosine similarity
        similarity_matrix = cosine_similarity(movie_ratings, movie_ratings)

        # Get movies similar to the user's preferences
        similar_movies = list(movie_ratings.columns)
        for movie_id, rating in self.user_preferences.items():
            similar_movies.remove(movie_id)

        recommendations = {}
        for movie in similar_movies:
            similarity_score = similarity_matrix[0, movie_ratings.columns.get_loc(movie)]
            weighted_score = sum(movie_ratings.loc[0, movie] * similarity_score for movie in similar_movies)
            recommendations[movie] = weighted_score

        # Sort and display top recommendations
        sorted_recommendations = sorted(recommendations.items(), key=lambda x: x[1], reverse=True)
        top_recommendations = [title for title, score in sorted_recommendations[:5]]

        tk.messagebox.showinfo("Top Recommendations", f"Top 5 recommended movies:\n{', '.join(top_recommendations)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = MovieRecommendationApp(root)
    root.mainloop()
