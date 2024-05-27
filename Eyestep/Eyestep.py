import os

class Eyestep:
    def __init__(self, path :str):
        """Generate a new eyestep analyzer

        Args:
            path (str): path to the executable
        """
        if os.path.exists(path):
            with open(path, "rb") as file:
                self.data = file.read()
                file.close()
        else:
            print("Error, no file supplied")

    def get_data(self):
        return self.data
