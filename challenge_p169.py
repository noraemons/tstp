class Shape:
    def what_am_i(self):
        print("I am a shape.")

class Rectangle(Shape):
    def __init__(self, w, l):
        self.width = w
        self.len = l

    def calculate_perimiter(self):
        return (self.width + self.len) * 2

a_rectangle = Rectangle(2, 4)
print(a_rectangle.calculate_perimiter())

class Square(Shape):
    def __init__(self, w):
        self.width = w

    def calculate_perimiter(self):
        return (self.width) * 4

    def chang_size(self, w):
        self.width = self.width + w

a_square = Square(2)
print(a_square.calculate_perimiter())


a_rectangle.what_am_i()
a_square.what_am_i()


class Horse:
    def __init__(self, rider):
        self.rider = rider

    def print_rider(self):
        print(self.rider.name)

class Rider:
    def __init__(self, name):
        self.name = name

a_rider = Rider("Jack")
a_horse = Horse(a_rider)

a_horse.print_rider()