#/usr/bin/python3
import temperature_sensor as ts
import time

# Main function
def main():
# Create a new temperature sensor object
    sensor = ts.TemperatureSensor(1, "Temperature Sensor 1")
    while True:
        print(sensor.get_value())
        time.sleep(sensor.get_updateTime())
        #send data to server
        sensor.notifyServer()




if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Exiting...")
        exit()
