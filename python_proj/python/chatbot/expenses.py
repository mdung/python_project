import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QPushButton, QTextEdit, QLineEdit
import sqlite3
from datetime import datetime

class FinanceManagerBot(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Finance Manager Bot")
        self.setGeometry(100, 100, 800, 600)

        # Database initialization
        self.connection = sqlite3.connect("finance_manager.db")
        self.create_tables()

        # GUI components
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout(self.central_widget)

        self.label = QLabel("Welcome to Finance Manager Bot", self)
        self.layout.addWidget(self.label)

        self.log_expense_button = QPushButton("Log Expense", self)
        self.log_expense_button.clicked.connect(self.log_expense)
        self.layout.addWidget(self.log_expense_button)

        self.set_budget_button = QPushButton("Set Budget", self)
        self.set_budget_button.clicked.connect(self.set_budget)
        self.layout.addWidget(self.set_budget_button)

        self.view_logs_button = QPushButton("View Expense Logs", self)
        self.view_logs_button.clicked.connect(self.view_expense_logs)
        self.layout.addWidget(self.view_logs_button)

        self.log_output = QTextEdit(self)
        self.log_output.setReadOnly(True)
        self.layout.addWidget(self.log_output)

    def create_tables(self):
        cursor = self.connection.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS expenses (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp TEXT NOT NULL,
                category TEXT NOT NULL,
                amount REAL NOT NULL
            )
        ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS budgets (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                category TEXT NOT NULL,
                amount REAL NOT NULL
            )
        ''')
        self.connection.commit()

    def log_expense(self):
        category, ok_pressed = QLineEdit.getText(
            QLineEdit(self), "Log Expense", "Enter expense category:")
        if ok_pressed and category:
            amount, ok_pressed = QLineEdit.getDouble(
                QLineEdit(self), "Log Expense", "Enter expense amount:")
            if ok_pressed:
                timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                self.save_expense(timestamp, category, amount)
                self.log_output.append(
                    f"Logged expense - {category}: ${amount} at {timestamp}")

    def save_expense(self, timestamp, category, amount):
        cursor = self.connection.cursor()
        cursor.execute('''
            INSERT INTO expenses (timestamp, category, amount) VALUES (?, ?, ?)
        ''', (timestamp, category, amount))
        self.connection.commit()

    def set_budget(self):
        category, ok_pressed = QLineEdit.getText(
            QLineEdit(self), "Set Budget", "Enter budget category:")
        if ok_pressed and category:
            amount, ok_pressed = QLineEdit.getDouble(
                QLineEdit(self), "Set Budget", "Enter budget amount:")
            if ok_pressed:
                self.save_budget(category, amount)
                self.log_output.append(
                    f"Set budget - {category}: ${amount}")

    def save_budget(self, category, amount):
        cursor = self.connection.cursor()
        cursor.execute('''
            INSERT OR REPLACE INTO budgets (category, amount) VALUES (?, ?)
        ''', (category, amount))
        self.connection.commit()

    def view_expense_logs(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM expenses")
        expenses = cursor.fetchall()

        self.log_output.clear()
        for expense in expenses:
            self.log_output.append(
                f"Expense ID: {expense[0]}, Category: {expense[2]}, Amount: ${expense[3]}, Timestamp: {expense[1]}")

        cursor.execute("SELECT * FROM budgets")
        budgets = cursor.fetchall()

        self.log_output.append("\nBudgets:")
        for budget in budgets:
            self.log_output.append(
                f"Budget ID: {budget[0]}, Category: {budget[1]}, Amount: ${budget[2]}")

    def closeEvent(self, event):
        self.connection.close()
        event.accept()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FinanceManagerBot()
    window.show()
    sys.exit(app.exec_())
