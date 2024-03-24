from time import sleep
from keyboard import send
import ctypes
import subprocess
from datetime import datetime, timedelta
from ez import notify, print_divider

def print_message(message, write_to_log=True, need_notification=False, title=""):
    # Show the timestamps for the corresponding status code
    current_datetime = datetime.now()
    formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
    # print timestamps with the message
    print(formatted_datetime, "|", message)

    if write_to_log:
        with open("./log.txt", "a", encoding="utf-8") as log:
            log.write(formatted_datetime + " | " + message + "\n")

    if need_notification is True:
        notify(title=title, message=message)


def launch_music_player() -> None:
    # r"" is used to convert the string to raw string
    music_player_path = r"C:\Program Files (x86)\NetEase\CloudMusic\cloudmusic.exe"
    subprocess.Popen(music_player_path)


def play_next_song() -> None:
    # Press "Ctrl+Alt+Right Arrow" to play the next song in my music player
    send('ctrl+alt+right')


def lock_screen():
    # Locks the screen on Windows
    ctypes.windll.user32.LockWorkStation()


def reminder(interval_minutes: float) -> None:
    while True:
        print_divider()

        next_rest_time = datetime.now() + timedelta(minutes=interval_minutes)
        print_message(f"Next break at {next_rest_time.strftime('%m-%d %H:%M:%S')}.")

        sleep(interval_minutes * 60)  # Convert minutes to seconds
        print_message("Time to take a break!", need_notification=True, title="Rest Reminder", write_to_log=False)

        launch_music_player()
        sleep(15)  # Give me some time to respond before playing songs suddenly 🤣
        play_next_song()
        print_message("Playing the next song.", write_to_log=False)

        sleep(15)
        print_message("Locking the screen...", write_to_log=False)
        lock_screen()

        sleep(5*60)  # 5 minutes break


if __name__ == "__main__":
    interval_minutes = float(input("Enter the reminder interval in minutes: "))
    reminder(interval_minutes)
