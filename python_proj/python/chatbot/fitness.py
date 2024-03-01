import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QPushButton, QTextEdit, QLineEdit
import sqlite3
from datetime import datetime

class HealthFitnessAdvisor(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Health and Fitness Advisor")
        self.setGeometry(100, 100, 600, 400)

        # Database initialization
        self.connection = sqlite3.connect("health_fitness.db")
        self.create_tables()

        # GUI components
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout(self.central_widget)

        self.label = QLabel("Welcome to Health and Fitness Advisor", self)
        self.layout.addWidget(self.label)

        self.workout_button = QPushButton("Log Workout", self)
        self.workout_button.clicked.connect(self.log_workout)
        self.layout.addWidget(self.workout_button)

        self.recipe_button = QPushButton("Get Healthy Recipe", self)
        self.recipe_button.clicked.connect(self.get_recipe)
        self.layout.addWidget(self.recipe_button)

        self.log_output = QTextEdit(self)
        self.log_output.setReadOnly(True)
        self.layout.addWidget(self.log_output)

    def create_tables(self):
        cursor = self.connection.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS workouts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp TEXT NOT NULL,
                exercise TEXT NOT NULL,
                duration INTEGER NOT NULL
            )
        ''')
        self.connection.commit()

    def log_workout(self):
        exercise, ok_pressed = QLineEdit.getText(
            QLineEdit(self), "Log Workout", "Enter exercise:")
        if ok_pressed and exercise:
            duration, ok_pressed = QLineEdit.getInt(
                QLineEdit(self), "Log Workout", "Enter duration (minutes):", 30, 1, 1440)
            if ok_pressed:
                timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                self.save_workout(timestamp, exercise, duration)
                self.log_output.append(
                    f"Logged workout - {exercise} for {duration} minutes at {timestamp}")

    def save_workout(self, timestamp, exercise, duration):
        cursor = self.connection.cursor()
        cursor.execute('''
            INSERT INTO workouts (timestamp, exercise, duration) VALUES (?, ?, ?)
        ''', (timestamp, exercise, duration))
        self.connection.commit()

    def get_recipe(self):
        # You can implement recipe retrieval logic here
        self.log_output.append("Fetching a healthy recipe...")

    def closeEvent(self, event):
        self.connection.close()
        event.accept()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = HealthFitnessAdvisor()
    window.show()
    sys.exit(app.exec_())
