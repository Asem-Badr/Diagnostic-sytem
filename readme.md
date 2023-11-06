# DIAGNOSTIC SYSTEM 
## this is a part of our ITI embedded system doploma graduation project 
the project we made is a car info diagnostic system
## the files in this repo
* bus_handler.py : this file reads diagnostic data from the I2C bus and organizes the data in data.json
* data.json :this file holds the data gathered from the bus
* publisher.py : this file sends the data from data.json file using mqtt protocol
* watch_dog.py : this file watches the json file ,each time the file content changes it calls the publisher
* run_diagnostic.sh : this file the process of running this part of the project


## how to run this part of the project
```bash 
bash run_diagnostic.sh
``` 

## A quick discription of this part of the project 
we have an I2C data bus which the ECUs of the car are connected to it. The ECUs sends diagnostic data on the bus 
the raspberry pi which this part of the project runs on are also connected to the bus. The information of the ECUs addresses are known to the raspberry pi. Each piece of information has a unique id which also is known to the raspberry. The raspberry requests these pieces of information form the ECUs and then parse it into a json format in the file called data.json. The data.json is watched by another process which is responsible for visualizing the data. The data also is needed in the customer service so we have to send the data.json through the cloud. in order not to send the data periodically which will cause high data traffic we created a watch_dog process to send the data only when there is a change in the data.json file.
