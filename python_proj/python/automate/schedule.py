import schedule
import time

def my_task():
    print("Scheduled task executed!")

# Schedule the task to run every 5 seconds
schedule.every(5).seconds.do(my_task)

# Run the scheduler
while True:
    schedule.run_pending()
    time.sleep(1)
