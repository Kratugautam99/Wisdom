import time
import winsound
from win10toast import ToastNotifier

def remind_to_drink_water(interval_hours: int):
    i = 0
    notifier = ToastNotifier()
    while True:
        if i == 0:
            interval_seconds = interval_hours*2
            time.sleep(interval_seconds)
            winsound.Beep(660, 1500)
            notifier.show_toast(
            "Drink Water Reminder",
            "It's time to drink water!",
            duration=10,
            threaded=True)
        else:
            interval_seconds = interval_hours * 60 * 60
            time.sleep(interval_seconds)
            winsound.Beep(660, 1500)
            notifier.show_toast(
            "Drink Water Reminder",
            "It's time to drink water!",
            duration=10,
            threaded=True)
        i += 1
remind_to_drink_water(1)
