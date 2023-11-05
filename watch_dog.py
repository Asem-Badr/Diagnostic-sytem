import os
import time
import subprocess

file_path = "./data.json"  # Replace with the path to your file
last_modified_time = os.path.getmtime(file_path)

while True:
    #getmtime system call returns the lastest modification time of the file
    current_modified_time = os.path.getmtime(file_path)
    #compare the time of the last modification with the current modification time
    if current_modified_time != last_modified_time:
        print(f'File {file_path} has been modified')
        #if the json file content is update call the publish the data through mqtt
        subprocess.call(["python3", "publish.py"]) 
        last_modified_time = current_modified_time
    time.sleep(1)
