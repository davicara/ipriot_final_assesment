"""





"""
import random
import time as task
import moondalup as Moondalup
import carpark as Carpark
import sensor as Sensor

def main():
    city = Moondalup.City()
    carpark = Carpark.Carpark(100, 9, 18)
    sensor = Sensor.Sensor(carpark)

    index = 1
    def update_index(index):
        if index == 10:
            city.update_city()
            return 1
        index += 1
        return index

    while True:
        index = update_index(index)

        num = random.randint(1, 1)
        if num == 1:
            if random.randint(1, 2) == 2:
                sensor.car_sensed(Carpark.Car(),"Arriving")
            else:
                if len(carpark.cars) > 0:
                    sensor.car_sensed(random.choice(carpark.cars), "Leaving")

        task.sleep(1)




if __name__ == "__main__":
    main()