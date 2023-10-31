
1- run the packages.sh to install all the required libs


#if you put this folder on your raspberry desktop it will work without changing any thing 

if you want to change the directory path ->


1- ON MQTT SERVICE YOU HAVE TO CHANGE THE FOLLWOING PATHS
    a- common_flag_file = "/home/karim/Desktop/Process/MQTT_SERVICE/common_flag.txt"


    b-file_path = f'/home/karim/Desktop/Process/MQTT_SERVICE/{file_name}' -> the files path that gonna receive the binary data

2- FIRMWARE SERVICE 


    a-def GetBinaryFilePath(signal):
    if signal == "0x1":
        return "/home/karim/Desktop/Process/MQTT_SERVICE/App.bin"
    elif signal == "0x2":
        return "/home/karim/Desktop/Process/MQTT_SERVICE/App1.bin"
    elif signal == "0x3":
        return "/home/karim/Desktop/Process/MQTT_SERVICE/App2.bin"
    else:
        return None

change those paths to the three .bin files which is receive the bin files from mqtt
