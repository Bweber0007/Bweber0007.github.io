# The Item class is used to hold the data for each item at the application level
# It is intended to provide a uniform and controlled way to access and manipulate the data

class Item:
    def __init__(self, name, frequency=1):
        self.name = name
        self.frequency = frequency

    def increment(self):
        self.frequency += 1

    def decrement(self):
        if self.frequency > 0:
            self.frequency -= 1

    def __str__(self):
        return f"{self.name:15} {self.frequency}"

    def __lt__(self, other):
        return self.frequency < other.frequency
