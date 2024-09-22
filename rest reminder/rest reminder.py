from time import sleep
from keyboard import send
import ctypes
import subprocess
from datetime import datetime, timedelta
from ez import notify, print_divider, get_info_path
from os.path import join

# r"" is used to convert the string to raw string
BROWSER_PATH = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
LOG_FILE_PATH = join(get_info_path(), "log.txt")


def print_message(message, write_to_log=True, need_notif=False, notif_title=""):
    current_datetime = datetime.now()
    formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
    print(formatted_datetime, "|", message)

    if write_to_log:
        with open(LOG_FILE_PATH, "a", encoding="utf-8") as log:
            log.write(formatted_datetime + " | " + message + "\n")

    if need_notif is True:
        notify(title=notif_title, message=message)


def launch_browser() -> None:
    """
    Open a new tab rather than a new window for easier closing
    """
    subprocess.Popen([BROWSER_PATH, "--new-tab"])


def play_next_song() -> None:
    """
    Press "Ctrl+Alt+Right Arrow" to play the next song in my music player
    """
    send("ctrl+alt+right")


def lock_screen():
    ctypes.windll.user32.LockWorkStation()


def reminder(interval_minutes: float) -> None:
    while True:
        print_divider()

        next_rest_time = datetime.now() + timedelta(minutes=interval_minutes)
        print_message(f"Next break at {next_rest_time.strftime('%m-%d %H:%M:%S')}.")

        sleep(interval_minutes * 60)  # Convert minutes to seconds
        print_message(
            f"Time to take a break! 🍵",
            write_to_log=False,
            need_notif=True,
            notif_title="Rest Reminder",
        )

        launch_browser()
        sleep(30)  # 30 second buffer time to wrap up the current task
        print_message("Locking the screen...", write_to_log=False)
        lock_screen()

        sleep(5 * 60)  # 5 minutes break


if __name__ == "__main__":
    interval_minutes = float(input("Enter the reminder interval in minutes: "))

    # separate the logs for each run
    with open(LOG_FILE_PATH, "a", encoding="utf-8") as log:
        log.write(f"{'='*10}")
        log.write(
            datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            + " | "
            + f"Rest reminder started with interval of {interval_minutes} minutes"
        )
        log.write(f"{'='*10}\n")

    reminder(interval_minutes)
