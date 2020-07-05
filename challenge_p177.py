class Shape:
    def what_am_i(self):
        print("I am a shape.")

class Square(Shape):
    square_list = []

    def __init__(self, w):
        self.width = w
        self.square_list.append(self)

    def calculate_perimiter(self):
        return (self.width) * 4

    def chang_size(self, w):
        self.width = self.width + w

    def __repr__(self):
        return "{} by {} by {} by {}".format(self.width, self.width, self.width, self.width)

s1 = Square(1)
s2 = Square(2)
s3 = Square(3)

print(Square.square_list)
print(s1)


def issame(object1, object2):
    if object1 is object2:
        return True
    else:
        return False

print(issame(s1, s2))
print(issame(s1, s1))