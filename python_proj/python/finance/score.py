import datetime
import pickle

class CreditScoreMonitoringSystem:
    def __init__(self):
        self.user_data = {}

    def register_user(self, user_id, name):
        """Register a new user in the system."""
        if user_id not in self.user_data:
            self.user_data[user_id] = {'name': name, 'credit_scores': []}
            print(f"User {user_id} ({name}) registered successfully.")
        else:
            print(f"User {user_id} already exists.")

    def record_credit_score(self, user_id, credit_score):
        """Record a new credit score for a user."""
        if user_id in self.user_data:
            timestamp = datetime.datetime.now()
            self.user_data[user_id]['credit_scores'].append({'timestamp': timestamp, 'score': credit_score})
            print(f"Credit score recorded for User {user_id}.")
        else:
            print(f"User {user_id} not found.")

    def view_credit_scores(self, user_id):
        """View credit scores history for a user."""
        if user_id in self.user_data:
            credit_scores = self.user_data[user_id]['credit_scores']
            if credit_scores:
                print(f"Credit Scores for User {user_id} ({self.user_data[user_id]['name']}):")
                for entry in credit_scores:
                    print(f"{entry['timestamp']}: {entry['score']}")
            else:
                print(f"No credit scores recorded for User {user_id}.")
        else:
            print(f"User {user_id} not found.")

    def save_data(self, filename):
        """Save user data to a file."""
        with open(filename, 'wb') as file:
            pickle.dump(self.user_data, file)
        print(f"Data saved to {filename}.")

    def load_data(self, filename):
        """Load user data from a file."""
        try:
            with open(filename, 'rb') as file:
                self.user_data = pickle.load(file)
            print(f"Data loaded from {filename}.")
        except FileNotFoundError:
            print(f"File {filename} not found. Starting with an empty database.")

def main():
    credit_monitor = CreditScoreMonitoringSystem()

    while True:
        print("\nCredit Score Monitoring System Menu:")
        print("1. Register User")
        print("2. Record Credit Score")
        print("3. View Credit Scores")
        print("4. Save Data")
        print("5. Load Data")
        print("6. Quit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            user_id = input("Enter user ID: ")
            name = input("Enter user name: ")
            credit_monitor.register_user(user_id, name)

        elif choice == '2':
            user_id = input("Enter user ID: ")
            credit_score = float(input("Enter credit score: "))
            credit_monitor.record_credit_score(user_id, credit_score)

        elif choice == '3':
            user_id = input("Enter user ID: ")
            credit_monitor.view_credit_scores(user_id)

        elif choice == '4':
            filename = input("Enter the filename to save data: ")
            credit_monitor.save_data(filename)

        elif choice == '5':
            filename = input("Enter the filename to load data: ")
            credit_monitor.load_data(filename)

        elif choice == '6':
            print("Exiting the Credit Score Monitoring System. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
