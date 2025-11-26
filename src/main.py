"""





"""
import random
import time as task
import moondalup as Moondalup
import carpark as Carpark
import sensor as Sensor
from display import Display


def main():
    city = Moondalup.City()
    display1 = Display("Entrance")
    display2 = Display("Weather")
    carpark = Carpark.Carpark(100, "Moondalup", [display1, display2])
    sensor = Sensor.Sensor(carpark)

    index = 1

    def update_index(index):
        if index == 10:
            city.update_city()
            carpark.update_temp(city.temperature, city.get_time(), display2)
            return 1
        index += 1
        return index

    while True:
        index = update_index(index)

        num = random.randint(1, 3)
        if num == 1:
            if random.randint(1, 3) <= 2:
                sensor.car_sensed(Carpark.Car(), "Arriving", display1)
            else:
                if len(carpark.cars) > 0:
                    sensor.car_sensed(random.choice(carpark.cars), "Leaving", display1)

        task.sleep(1)




if __name__ == "__main__":
    main()
