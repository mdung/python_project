import datetime
import os

def log_activity(activity, duration):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"{timestamp} - {activity}: {duration} minutes\n"

    with open("fitness_log.txt", "a") as log_file:
        log_file.write(log_entry)

def display_log():
    if os.path.exists("fitness_log.txt"):
        with open("fitness_log.txt", "r") as log_file:
            print(log_file.read())
    else:
        print("No fitness data available.")

def main():
    print("Fitness Tracking System")

    while True:
        print("\n1. Log Activity")
        print("2. Display Log")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            activity = input("Enter the activity: ")
            duration = float(input("Enter the duration (minutes): "))
            log_activity(activity, duration)
            print("Activity logged successfully!")

        elif choice == "2":
            print("\nFitness Log:")
            display_log()

        elif choice == "3":
            print("Exiting Fitness Tracking System. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
