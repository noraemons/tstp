class Shape:
    def __init__(self, w, l):
        self.width = w
        self.len = l

    def print_size(self):
        print("{} by {}".format(self.width, self.len))

class Square(Shape):
    #inheriting Shape class
    def area(self):
        return self.width * self.len

    def print_size(self):
        print("I am {} by {}".format(self.width, self.len))
        #method override

square1 = Square(5, 10)
square1.print_size()
print(square1.area())