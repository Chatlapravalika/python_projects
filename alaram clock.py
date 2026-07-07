from datetime import datetime
import time

# Alarm time input
alarm_time = input("Enter alarm time (HH:MM:SS): ")

print(f"Alarm set for {alarm_time}")
print("Waiting...")

while True:
    current_time = datetime.now().strftime("%H:%M:%S")
    print(current_time, end="\r")

    if current_time == alarm_time:
        print("\n⏰ WAKE UP! Alarm Time Reached!")

        # For Windows
        try:
            import winsound
            for _ in range(5):
                winsound.Beep(1000, 500)  # Frequency, Duration
                time.sleep(0.5)
        except:
            print("\a")  # Terminal beep for other OS

        break

    time.sleep(1)