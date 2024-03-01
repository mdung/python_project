import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QPushButton, QTextEdit, QLineEdit
import sqlite3
from datetime import datetime

class TravelAssistant(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Travel Assistant")
        self.setGeometry(100, 100, 800, 600)

        # Database initialization
        self.connection = sqlite3.connect("travel_assistant.db")
        self.create_tables()

        # GUI components
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout(self.central_widget)

        self.label = QLabel("Welcome to Travel Assistant", self)
        self.layout.addWidget(self.label)

        self.plan_trip_button = QPushButton("Plan Trip", self)
        self.plan_trip_button.clicked.connect(self.plan_trip)
        self.layout.addWidget(self.plan_trip_button)

        self.view_logs_button = QPushButton("View Trip Logs", self)
        self.view_logs_button.clicked.connect(self.view_trip_logs)
        self.layout.addWidget(self.view_logs_button)

        self.log_output = QTextEdit(self)
        self.log_output.setReadOnly(True)
        self.layout.addWidget(self.log_output)

    def create_tables(self):
        cursor = self.connection.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS trips (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp TEXT NOT NULL,
                destination TEXT NOT NULL,
                accommodation TEXT NOT NULL,
                attractions TEXT NOT NULL
            )
        ''')
        self.connection.commit()

    def plan_trip(self):
        destination, ok_pressed = QLineEdit.getText(
            QLineEdit(self), "Plan Trip", "Enter destination:")
        if ok_pressed and destination:
            accommodation, ok_pressed = QLineEdit.getText(
                QLineEdit(self), "Plan Trip", "Enter accommodation:")
            if ok_pressed and accommodation:
                attractions, ok_pressed = QLineEdit.getText(
                    QLineEdit(self), "Plan Trip", "Enter tourist attractions (comma-separated):")
                if ok_pressed and attractions:
                    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    self.save_trip(timestamp, destination, accommodation, attractions)
                    self.log_output.append(
                        f"Planned trip to {destination} with accommodation at {accommodation}. Attractions: {attractions} ({timestamp})")

    def save_trip(self, timestamp, destination, accommodation, attractions):
        cursor = self.connection.cursor()
        cursor.execute('''
            INSERT INTO trips (timestamp, destination, accommodation, attractions) VALUES (?, ?, ?, ?)
        ''', (timestamp, destination, accommodation, attractions))
        self.connection.commit()

    def view_trip_logs(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM trips")
        trips = cursor.fetchall()

        self.log_output.clear()
        for trip in trips:
            self.log_output.append(
                f"Trip ID: {trip[0]}, Destination: {trip[2]}, Accommodation: {trip[3]}, Attractions: {trip[4]}, Timestamp: {trip[1]}")

    def closeEvent(self, event):
        self.connection.close()
        event.accept()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TravelAssistant()
    window.show()
    sys.exit(app.exec_())
