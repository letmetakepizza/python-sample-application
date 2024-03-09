class Car:

    is_new = True

    def __init__(self, model, year, colour):
        self.model = model
        self.year = year
        self.colour = colour
        self.mileage = 0

    def condition(self, name):
        if self.is_new:
            return "New"
        else:
            return "Used"

    def drive(self, distance):
        self.is_new = False
        self.mileage += distance

    def description(self, name):
        condition = self.condition('test')
        print(f"This {self.model} was made in {self.year}.\n"
              f"It is {self.colour} and its condition is {condition}.")
