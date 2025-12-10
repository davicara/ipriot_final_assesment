import random
from src.log_book import LogBook
from src.display import Display

license_plates = [
    "ABC1234", "XYZ5678", "LMN9876", "QWE2345", "PQR6789",
    "1234XYZ", "AB12CDE", "GHI4567", "JKL7890", "MN12OPQ",
    "TUV3456", "RST2345", "OPQ6789", "MNO1234", "4567DEF",
    "FQR8901", "ZXY5678", "PQR2345", "KLM1234", "UVW5678",
    "D12GHI3", "7890JKL", "LMN3456", "DEF6789", "JK4567P",
    "QWERTY1", "A123BCD", "1234ABC", "QZX5671", "DFG9876",
    "QWE8765", "JK9876P", "T123456", "OPQ5432", "XYZ2468",
    "R4321LM", "123XYZ4", "WXYZ234", "N123XYZ", "9870ABC",
    "ABCD567", "123ABC4", "XYZ3451", "PQR6780", "123ZXY8",
    "567ABC1", "T123LMN", "2345XYZ", "8765JKL", "LMNO890",
    "QWERT567", "D67FGHI", "R12345Q", "JK56789", "LMN2347",
    "8765PQR", "ZXY5679", "ABC2345", "LMN6789", "PQR1234",
    "GH34567", "JKL45689", "1234XYZ", "LMN3456", "NOP5678",
    "XY98765", "PQ123456", "RST3457", "LQW8765", "YZ123456",
    "987XYZ1", "L098JKO", "POQ4567", "XYZ78901", "T45LMN89",
    "AB56CDE", "FGH1234", "ZXY4321", "QWE1347", "JLM1234",
    "RT78901", "ABQ2345", "LMN4567", "KZ123QW", "GHI78901",
    "987ABC1", "234LMN9", "XY5678Z", "1234PQ5", "D234567",
    "OPQ8901", "RST2347", "LM3456P", "J123456", "789XYZ0"
]


def generate_plate():
    if len(license_plates) == 0:
        print("No more license plates available")
        return "DEFAULT PLATE"
    index = random.randint(0, (len(license_plates)-1))
    chosen_plate = license_plates[index]
    license_plates.remove(chosen_plate)

    return chosen_plate

class Car:
    _cars = {}

    def __new__(cls, plate=None, *args, **kwargs):
        if not plate:
            car = super().__new__(cls)
            car.plate = generate_plate()
            return car
        else:
            if plate in cls._cars:
                return cls._cars[plate]
            else:
                car = super().__new__(cls)
                car.plate = plate
                return car

    def __init__(self, plate=None):
        if not hasattr(self, "_initialized"):
            # self.plate = plate
            self._initialized = True


class Carpark:

    def __init__(self, bays, location, displays: []):
        self.location = location
        self.bays = bays
        self.occupied_bays = 0
        self.cars = []
        self.displays = displays or []
        self.entrance_display = Display()
        self.temp_display = Display()
        self.log_book = LogBook("car_park_"+location)

    def get_available_bays(self):

        return self.bays - self.occupied_bays

    def add_car(self, _car: Car, display: Display = None):
        if not display:
            display = self.displays[1]

        if self.get_available_bays() == 0:
            return

        self.log_book.log_object(_car)
        self.cars.append(_car)
        self.occupied_bays += 1

        if self.get_available_bays() == 0:
            display.update_display("No Bays Available, Carpark Locked")
        else:
            display.update_display(f"{self.get_available_bays()}/{self.bays} bays are currently available")

    def remove_car(self, _car: Car, display: Display = None):
        if not display:
            display = self.displays[1]
        if _car not in self.cars:
            raise ValueError("Car does not exist in carpark")

        self.cars.remove(_car)
        self.occupied_bays -= 1

        display.update_display(f"{self.get_available_bays()}/{self.bays} bays are currently available")
        license_plates.append(_car.plate)

    def update_temp(self, temp: float, time: int, display: Display):
        display.update_display(f"Current Temperature: {temp}C\nCurrent Time: {time}")


if __name__ == "__main__":
    pass

