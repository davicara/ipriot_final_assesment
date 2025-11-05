from display import Display


class Carpark:

    def __init__(self, bays):
        self.bays = bays
        self.occupied_bays = 0
        self.cars = []
        self.display = Display()


    def get_available_bays(self):
        return self.bays - self.occupied_bays
    def add_car(self, car):
        self.cars.append(car)
        self.occupied_bays += 1

        if self.get_available_bays() == 0:
            self.display.update_display("No Bays Available, Carpark Locked")
        else:
            self.display.update_display(f"{self.get_available_bays()}/{self.bays} bays are currently available")


    def remove_car(self, car):
        self.cars.remove(car)
        self.occupied_bays -= 1

        self.display.update_display(f"{self.get_available_bays()}/{self.bays} bays are currently available")

