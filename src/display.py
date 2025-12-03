import math

displays = {}
class Display:

    id = 0

    def __init__(self, name=len(displays)):
       # if displays[name]:
       #     print("ERROR: Cannot create multiple displays with same name")

        displays[name] = self
        self.id = name
        self.message = ""

    def update_display(self, message: str):

        self.message = message
        new_text = message.split("\n")
        length = len(message)

        if len(new_text) > 1:
            largest_length = 0
            largest_message = ""
            for text in new_text:
                if len(text) > largest_length:
                    largest_length = len(text)
                    largest_message = text

            length = largest_length

        prefix: str = f"Displaying On Display {self.id}"
        length: int = round((length-len(prefix))/2)

        if length <= 0:
            length = 2
            prefix = f"{"*" * length} {prefix} {"*" * length}"
            message = f"{" " * round(((len(prefix)-len(message))/2))}{message}"
        else:
            prefix = f"{"*" * length} {prefix} {"*" * length}"

        print(prefix)
        print(message)
        print(len(prefix)*"*")

    @classmethod
    def get_display(cls, name):
        if displays[name]:
            return displays[name]
        else:
            print("No Display Found")
