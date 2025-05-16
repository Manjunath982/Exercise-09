import time
from plyer import notification

def remind_to_drink_water():
    while True:
        notification.notify(
            title="Time to Drink Water!",
            message="Stay hydrated! It's time to drink a glass of water.",
            app_name="Water Reminder",
            timeout=10
        )
        time.sleep(2)

if __name__ == "__main__":
    remind_to_drink_water()
