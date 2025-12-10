import os.path
from pathlib import Path
import json


class LogBook:
    def __init__(self, log_name):
        self.log = Path(fr"./{log_name}.json")

        if not os.path.exists(self.log):
            open_file = open(self.log, "w+")
            json.dump({}, open_file, indent=4)
            open_file.close()

    def _load_json(self, form):
        print(self.log)
        open_file = open(self.log, form)
        try:
            data = json.load(open_file)
            return open_file, data
        except:
            return open_file, {}

    def log_object(self, car):
        open_file, data = self._load_json("w")
        data[car.plate] = car.plate
        json.dump(data, open_file, indent=4)
        open_file.close()

    def get_object(self, plate: str):
        open_file, data = self._load_json("r")

        if data[plate]:
            return data[plate]
        else:
            print(f"Car with plate: {plate} is not saved in the json file")
        open_file.close()

    def remove_object(self, plate: str):
        open_file, data = self._load_json("w")

        if data[plate]:
            data[plate] = None
            json.dump(data, open_file, indent=4)
        open_file.close()

    def print_log(self):
        open_file = open(self.log, "r")
        print(self.log)
        try:
            data = json.load(open_file)
        except Exception as err:
            print(err)
            open_file.close()
            return

        for plate, car in data.items():
            print(f"{plate}: {car}")
        open_file.close()
