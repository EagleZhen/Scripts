from time import sleep
from keyboard import send
import ctypes
import subprocess
from datetime import datetime, timedelta
from ez import notify, print_divider


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
        print(f"Next break at {next_rest_time.strftime('%m-%d %H:%M:%S')}.")

        sleep(interval_minutes * 60)  # Convert minutes to seconds
        notify(title="Rest Reminder", message="Time for a break!")

        launch_music_player()
        sleep(10)  # Give me some time to respond before playing songs suddenly 🤣
        play_next_song()
        print("Playing next song")

        sleep(10)
        print("Locking screen")
        lock_screen()

        sleep(5*60)  # 5 minutes break


if __name__ == "__main__":
    interval_minutes = float(input("Enter the reminder interval in minutes: "))
    reminder(interval_minutes)
