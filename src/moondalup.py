import time as task
import random

def lerp(start: float, end: float, t: float) -> float:
    """
    Linearly interpolates between start and end by t.

    Parameters:
        start (float): The starting value.
        end (float): The ending value.
        t (float): Interpolation factor (0.0 = start, 1.0 = end).
                   Values outside [0, 1] will extrapolate.

    Returns:
        float: Interpolated value.
    """
    # Validate inputs
    if not isinstance(start, (int, float)) or not isinstance(end, (int, float)):
        raise TypeError("start and end must be numbers (int or float).")
    if not isinstance(t, (int, float)):
        raise TypeError("t must be a number (int or float).")

    return start + (end - start) * t


days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
class City:

    day_count = 1
    day = days[day_count]
    time: int = 0
    temperature = 20
    min: int
    max: int
    hours = 24

    def __init__(self):
        self.min = random.randint(-5, 10)
        self.max = random.randint(10, 30)

    def update_day(self):
        if self.day_count == 6:
            self.day_count = 0
        else:
            self.day_count += 1

    def update_city(self):
        current_time: int
        if self.time > 12:
            current_time = 12 - (self.time - 12)
        else:
            current_time = self.time
        self.temperature = lerp(self.min, self.max, current_time / 12)
        print(self.temperature)

        self.time += 1

        if self.time == 25:
            self.time = 0
            self.min = random.randint(-5, 10)
            self.max = random.randint(10, 30)

    def get_day(self):
        return days[self.day_count]

    def get_time(self):
        return self.time


##if __name__ == "__main__":


