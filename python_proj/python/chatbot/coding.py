import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QPushButton, QTextEdit, QLineEdit, QFileDialog
import sqlite3
from datetime import datetime

class CodingHelperBot(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Coding Helper Bot")
        self.setGeometry(100, 100, 800, 600)

        # Database initialization
        self.connection = sqlite3.connect("coding_helper.db")
        self.create_tables()

        # GUI components
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout(self.central_widget)

        self.label = QLabel("Welcome to Coding Helper Bot", self)
        self.layout.addWidget(self.label)

        self.ask_question_button = QPushButton("Ask Coding Question", self)
        self.ask_question_button.clicked.connect(self.ask_question)
        self.layout.addWidget(self.ask_question_button)

        self.view_snippets_button = QPushButton("View Code Snippets", self)
        self.view_snippets_button.clicked.connect(self.view_code_snippets)
        self.layout.addWidget(self.view_snippets_button)

        self.log_output = QTextEdit(self)
        self.log_output.setReadOnly(True)
        self.layout.addWidget(self.log_output)

    def create_tables(self):
        cursor = self.connection.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS code_snippets (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp TEXT NOT NULL,
                language TEXT NOT NULL,
                code TEXT NOT NULL,
                description TEXT
            )
        ''')
        self.connection.commit()

    def ask_question(self):
        code_snippet, ok_pressed = QFileDialog.getOpenFileName(
            self, "Ask Coding Question", "", "Code Files (*.py *.java *.cpp);;All Files (*)"
        )
        if ok_pressed and code_snippet:
            with open(code_snippet, 'r') as file:
                code_content = file.read()

            language, ok_pressed = QLineEdit.getText(
                QLineEdit(self), "Ask Coding Question", "Enter programming language:")
            if ok_pressed and language:
                description, ok_pressed = QLineEdit.getText(
                    QLineEdit(self), "Ask Coding Question", "Enter question/description:")
                if ok_pressed:
                    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    self.save_code_snippet(timestamp, language, code_content, description)
                    self.log_output.append(
                        f"Question asked in {language}: {description} ({timestamp})")

    def save_code_snippet(self, timestamp, language, code, description):
        cursor = self.connection.cursor()
        cursor.execute('''
            INSERT INTO code_snippets (timestamp, language, code, description) VALUES (?, ?, ?, ?)
        ''', (timestamp, language, code, description))
        self.connection.commit()

    def view_code_snippets(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM code_snippets")
        snippets = cursor.fetchall()

        self.log_output.clear()
        for snippet in snippets:
            self.log_output.append(
                f"Snippet ID: {snippet[0]}, Language: {snippet[2]}, Description: {snippet[4]}, Timestamp: {snippet[1]}")

    def closeEvent(self, event):
        self.connection.close()
        event.accept()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CodingHelperBot()
    window.show()
    sys.exit(app.exec_())
