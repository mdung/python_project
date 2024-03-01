import schedule
import time

def daily_task():
    # Define the task you want to automate here
    print("Automated daily task is running!")

# Schedule the task to run every day at a specific time (e.g., 08:00 AM)
schedule.every().day.at("10:18").do(daily_task)

# You can add more tasks and schedules if needed

while True:
    # Run pending scheduled tasks
    schedule.run_pending()
    time.sleep(1)
