import sys
import sqlite3
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QPushButton, QTextEdit, QLineEdit, QComboBox
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
import pandas as pd
import random

class BookRecommendationBot(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Book Recommendation Bot")
        self.setGeometry(100, 100, 800, 600)

        # Database initialization
        self.connection = sqlite3.connect("book_recommendation.db")
        self.create_tables()

        # Load book data and TF-IDF vectorizer
        self.books_df = pd.read_csv("books.csv")
        self.vectorizer = TfidfVectorizer(stop_words='english')
        self.tfidf_matrix = self.vectorizer.fit_transform(self.books_df['description'].fillna(''))

        # GUI components
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout(self.central_widget)

        self.label = QLabel("Welcome to Book Recommendation Bot", self)
        self.layout.addWidget(self.label)

        self.preference_label = QLabel("Select your favorite genre:", self)
        self.layout.addWidget(self.preference_label)

        self.genre_combobox = QComboBox(self)
        self.genre_combobox.addItems(self.books_df['genre'].unique())
        self.layout.addWidget(self.genre_combobox)

        self.recommend_button = QPushButton("Get Book Recommendations", self)
        self.recommend_button.clicked.connect(self.get_recommendations)
        self.layout.addWidget(self.recommend_button)

        self.log_output = QTextEdit(self)
        self.log_output.setReadOnly(True)
        self.layout.addWidget(self.log_output)

    def create_tables(self):
        cursor = self.connection.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS user_preferences (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                genre TEXT NOT NULL
            )
        ''')
        self.connection.commit()

    def get_recommendations(self):
        genre = self.genre_combobox.currentText()
        if not genre:
            self.log_output.append("Please select a genre.")
            return

        self.save_user_preference(genre)
        self.log_output.append(f"Your favorite genre is set to: {genre}")

        recommendations = self.generate_book_recommendations(genre)
        if recommendations:
            self.log_output.append("\nRecommended Books:")
            for recommendation in recommendations:
                self.log_output.append(f"{recommendation['title']} - {recommendation['author']}")
        else:
            self.log_output.append("No recommendations found for this genre.")

    def save_user_preference(self, genre):
        cursor = self.connection.cursor()
        cursor.execute('''
            INSERT OR REPLACE INTO user_preferences (id, genre) VALUES (1, ?)
        ''', (genre,))
        self.connection.commit()

    def get_user_preference(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT genre FROM user_preferences WHERE id = 1")
        result = cursor.fetchone()
        return result[0] if result else None

    def generate_book_recommendations(self, user_genre):
        user_preference = self.get_user_preference()
        if not user_preference:
            return []

        # Filter books of the same genre as the user's preference
        genre_books = self.books_df[self.books_df['genre'] == user_preference]

        # Calculate the TF-IDF matrix for the genre books
        tfidf_matrix_genre = self.vectorizer.transform(genre_books['description'].fillna(''))

        # Calculate the cosine similarity between the user's genre and other books
        cosine_similarities = linear_kernel(tfidf_matrix_genre, self.tfidf_matrix)

        # Get indices of books with high similarity
        similar_books_indices = list(enumerate(cosine_similarities[-1]))

        # Sort the books based on similarity scores
        similar_books_indices.sort(key=lambda x: x[1], reverse=True)

        # Get the top 5 similar books
        recommended_books_indices = [index for index, _ in similar_books_indices[1:6]]

        # Retrieve book details
        recommendations = []
        for index in recommended_books_indices:
            recommendations.append({
                'title': self.books_df['title'].iloc[index],
                'author': self.books_df['author'].iloc[index]
            })

        return recommendations

    def closeEvent(self, event):
        self.connection.close()
        event.accept()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = BookRecommendationBot()
    window.show()
    sys.exit(app.exec_())
