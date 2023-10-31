import json
import smbus
import time
json_file_path = "data.json"
keys = [
        "coolant_sensor_state",
        "coolant_sensor_value",
        "oil_pressure_sensor_state",
        "oil_pressure_sensor_value",
        "break_wear_sensor_state",
        "break_fluid_sensor_state",
        "break_fluid_sensor_value",
        "ambient_temperature_sensor_value",
        "rain_sensor_value"
    ]
values = [
    0,0,0,0,0,0,0,0,0
    ]



#each sub list contains the pieces of information that we want to read from the each mcu
mcu_related_info_numbers = [[1,2,3,4],[5,6,7],[8,9]]
#each element in the list is the i2c address of the each mcu
mcus_addresses = [0x48 , 0x48 ,0x48]

def update_json(json_file_path, values , keys):
    with open(json_file_path, 'r') as file:
        data = json.load(file)
        for i in range(len(keys)):
            #check if the value changed
            if data[keys[i]] != values[i]:
                data[keys[i]] = values[i]
                with open(json_file_path, 'w') as file:
                    json.dump(data, file, indent=4)


def read_sensors( values, mcus_addresses):
    bus = smbus.SMBus(0)
    for i in range(len(mcus_addresses)):
        sensor_address = mcus_addresses[i]
        try:
            for j in range(len(mcu_related_info_numbers[i])):
                sensor_value = bus.read_byte(sensor_address)
                print(sensor_value ,end='\t')
                #check if the value is in the list of the values that we want to read the following byte
                if(sensor_value == mcu_related_info_numbers[i][j]):
                    sensor_value = bus.read_byte(sensor_address)
                    print(sensor_value,end='\n')
                    values[(mcu_related_info_numbers[i][j])-1] = sensor_value
        except IOError:
            print("Error: Check if the sensor is connected properly.")
            return None


def main():
    while True:
        read_sensors( values, mcus_addresses)
        #we should check if the values changed first and then update the json file
        #this change can be indicated by a flag
        update_json(json_file_path, values, keys)
        time.sleep(1)  

if __name__ == '__main__':
    main()

