import re
import os
import json
import ez
from send2trash import send2trash


def convert_to_milliseconds(time_str: str) -> int:
    """Convert HH:MM:SS format to milliseconds"""
    hours, minutes, seconds = map(int, time_str.split(":"))
    return (hours * 3600 + minutes * 60 + seconds) * 1000


def parse_infowriter_content(content: str) -> list[tuple]:
    """Parse the .infowriter content, return a list of unique milliseconds"""
    # ^ and $ are used to match the start and end of the line respectively
    # . matches any character except a newline
    # * matches 0 or more occurrences of the preceding character
    # ? makes the match non-greedy to ensure that it stops at the end of the current line
    # re.MULTILINE is used to match the start and end of each line in a multi-line string

    # [1:-1] Discard the meaningless first and last bookmarks that is always 0:00:00
    captured_groups = re.findall(
        r"^(\d+:\d+:\d+).(.*?)$", content, re.MULTILINE)[1:-1]
    # print(captured_groups)

    # Convert time markers to milliseconds and store them in a list of tuples
    default_text = "Record Time Marker"
    time_markers = [(convert_to_milliseconds(
        time), (text if text != default_text else "")) for time, text in captured_groups]

    # Sort the list of tuples by milliseconds
    sorted_time_markers = sorted(time_markers, key=lambda x: x[0])

    # This will be an empty list if there are no manually added time markers
    return sorted_time_markers


def write_to_pbf(sorted_time_markers: list, output_file: str) -> None:
    """Convert the bookmarks into format of .pbf file"""
    with open(output_file, "w", encoding="utf-8") as file:
        file.write("[Bookmark]\n")
        for i, (ms, text) in enumerate(sorted_time_markers):
            file.write(f"{i}={ms}*{text}*\n")


def convert_infowriter_to_pbf(input_file: str, output_file: str) -> None:
    """Convert .infowriter file to .pbf format"""
    with open(input_file, "r", encoding="utf-8") as file:
        content = file.read()

    sorted_time_markers = parse_infowriter_content(content)
    if sorted_time_markers != []:  # Only write to .pbf if there are meaningful time markers
        write_to_pbf(sorted_time_markers, output_file)


def find_infowriter_files(directory_path: str) -> list:
    """Find all .infowriter files in the given directory."""
    infowriter_files = []
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            if file.endswith(".infowriter"):
                infowriter_files.append(os.path.join(root, file))
    return infowriter_files


def batch_convert_infowriter_to_pbf(directory_path: str) -> None:
    """Convert all .infowriter files in the directory to .pbf format."""
    infowriter_file_list = find_infowriter_files(directory_path)

    # Print the .infowriter files found to confirm
    ez.print_divider()
    for file in infowriter_file_list:
        print(f"{file}")
    ez.print_divider()

    # Confirm performing the conversion
    confirm = input("Do you want to convert these files to .pbf? ([y]/n): ")
    if confirm.lower() == "n":
        print("Cancelling conversion...")
        return

    for file in infowriter_file_list:
        # Get the file name and append .pbf extension
        output_file = os.path.splitext(file)[0] + ".pbf"
        convert_infowriter_to_pbf(file, output_file)
    print("Converted .infowriter files to .pbf if there are meaningful time markers.")

    # Confirm moving the .infowriter files to trash
    confirm = input(
        "Do you want to move the .infowriter files to trash? (y/[n]): ")
    if confirm.lower() != "y":
        print("Skipping deletion...")
        return

    send2trash(infowriter_file_list)
    print("Moved .inforwriter files to trash.")


def read_directory_path_from_json(json_file: str) -> str:
    """Read the directory path from a JSON file."""
    with open(json_file, "r", encoding="utf-8") as file:
        info = json.load(file)
    return info["Path"]


if __name__ == "__main__":
    """
    Assume the JSON file has a structure like: {"Path": "\\path\\to\\directory"}
    Must be \\ instead of /, otherwise send2trash will not work
    """
    info_file_path = os.path.join(ez.get_info_path(), "info.json")
    directory_path = read_directory_path_from_json(info_file_path)
    print(f"Directory path: {directory_path}")
    batch_convert_infowriter_to_pbf(directory_path)

    os.system("pause")
