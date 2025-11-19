

displays = []
class Display:

    id = 0

    def __init__(self):
        displays.append(self)
        self.id = len(displays)

    def update_display(self, message: str):
        prefix: str = f"Displaying On Display {self.id}"
        length: int = round((len(message)-len(prefix))/2)

        if length <= 0:
            length = 2
            prefix = f"{"*" * length} {prefix} {"*" * length}"
            message = f"{" " * round(((len(prefix)-len(message))/2))}{message}"
        else:
            prefix = f"{"*" * length} {prefix} {"*" * length}"

        print(prefix)
        print(message)
        print(len(prefix)*"*")
