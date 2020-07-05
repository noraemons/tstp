import math

class Apple:
    def __init__(self, size, weight, color, sugar):
        self.size = size
        self.weight = weight
        self.color = color
        self.sugar = sugar

class Circle():
    def __init__(self, r):
        self.rad = r

    def calc_area(self):
        return self.rad ** 2 * math.pi

a_circle = Circle(10)
print(a_circle.calc_area())

class Triangle():
    def __init__(self, b, h):
        self.base = b
        self.height = h

    def calc_area(self):
        return self.base * self.height / 2

a_triangle = Triangle(10, 5)
print(a_triangle.calc_area())

class EquHexagon():
    def __init__(self, r):
        self.rad = r

    def calc_perimeter(self):
        return self.rad * 6

a_equhexagon = EquHexagon(5)
print(a_equhexagon.calc_perimeter())