#!/bin/python3
import os
import time
import pyperclip
from datetime import datetime
import subprocess

# Location of the file where the clipboard log is stored.
# "/dev/smb" is a temporary location(Saved in RAM) which is cleared when the system reboots
LOG_FILE = "/dev/shm/clipboard_log.txt"

# Check if the previous index exists
def get_previous_index_value():
    try:
        # Using subprocess to capture the output
        command = f'tail -n 20 {LOG_FILE} | grep "Entry No" | awk -F": " \'{{print $2}}\' | tail -n 1'
        result = subprocess.check_output(command, shell=True).decode().strip()

        # Convert the result to an integer and increment
        LAST_INDEX = int(result) if result else 0
        INDEX = LAST_INDEX + 1
        return INDEX
    except Exception as e:
        print(f"Error occured: {e}")                                                            
        
# If any file is copied, this function gets the details of the file and saves it into the log
# https://www.geeksforgeeks.org/python-os-stat-method/
def get_file_info(path):
    try:
        stat = os.stat(path)
        return {
            'Name': os.path.basename(path),
            'Location': os.path.abspath(path),
            'Size': f"{stat.st_size} bytes",
            # The time.ctime() function in Python converts a time (expressed in number of seconds) into a human-readable string format.
            'Created': time.ctime(stat.st_ctime),
            'Modified': time.ctime(stat.st_mtime)
        }
    except Exception as e:
        print(f"An error occured: {e}")

# Writing the clipboard log on to the temporary file
def write_to_log_file(index, content):
    with open(LOG_FILE, 'a') as f:
        f.write(f"{'=' * 60}\n")
        f.write(f"Entry No: {index}\n")
        f.write(f"Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(content + "\n")


# This function opens the Log file in a text editor of your choice
def open_in_text_editor():

    # Try to open the text editor
    try:
        TEXT_EDITOR = 'mousepad'
        subprocess.Popen([TEXT_EDITOR, LOG_FILE])          
    except Exception as e:
        print(f"Error occured: {e}")


# Check if the copied data is a file path, not a directory
def is_file_path(COPIED_FILE_PATH):
    return os.path.exists(COPIED_FILE_PATH) and os.path.isfile(COPIED_FILE_PATH)

def clipboard_monitor():
    global INDEX
    while True:
        try:
            open_in_text_editor()
            # It will wait until new data is copied
            # https://pyperclip.readthedocs.io/en/latest/
            COPIED_DATA = pyperclip.waitForNewPaste()
            # Copies the clipboard data to the variable
            if is_file_path(COPIED_DATA):
                    # If it is a file path the getting the file stats
                    file_info = get_file_info(COPIED_DATA)
                    CONTENT = '\n'.join([f"{k}: {v}" for k, v in file_info.items()])
            else:
                CONTENT = f"Copied Text: {COPIED_DATA}"
            # Writing the chnges to the log file
            INDEX = get_previous_index_value()
            write_to_log_file(INDEX, CONTENT)
            subprocess.reload
            INDEX += 1               

        except KeyboardInterrupt:
            print("\nClip Logger has been stopped.")
            break
        except Exception as e:
            print(f"Error occured: {e}")

if __name__ == "__main__":
    try:
        print("Clip Logger has started.")
        # Check if the log file already exist, if not then create one
        if os.path.isfile(LOG_FILE):
            clipboard_monitor()
        else:
            with open(LOG_FILE, 'a'):  # Create the file if it doesn't exist
                clipboard_monitor()

    except KeyboardInterrupt:
        print("\nProgram terminated by user.")

