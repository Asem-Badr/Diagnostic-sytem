import os
import time
import subprocess

file_path = "./data.json"  # Replace with the path to your file
last_modified_time = os.path.getmtime(file_path)

while True:
    time.sleep(1)
    current_modified_time = os.path.getmtime(file_path)
    if current_modified_time != last_modified_time:
        print(f'File {file_path} has been modified')
        subprocess.call(["python3", "publish.py"])  # Replace with the path to your script
        last_modified_time = current_modified_time
