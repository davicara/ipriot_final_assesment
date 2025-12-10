import carpark


class Sensor:

    def __init__(self, _carpark: carpark.Carpark):
        self.name = "Sensor"
        self.carpark = _carpark

    def car_sensed(self, car: carpark.Car, state: str, display):
        # car = carpark.Car(car.plate)
        if state == "Arriving":
            self.carpark.add_car(car, display)
        elif state == "Leaving":
            self.carpark.remove_car(car, display)

