class Shape:
    def __init__(self):
        pass

    def area(self):
        return self.area


class Square(Shape):
    def __init__(self, length):
        super().__init__()
        self.length = length

    def area(self):
        return self.length * self.length


square = Square(3)
print('정사각형의 면적: {}'.format(square.area()))
