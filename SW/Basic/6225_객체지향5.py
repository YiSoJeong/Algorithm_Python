class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def print_area(self):
        print('사각형의 면적: {}'.format(self.width*self.height))


# int로 전달
rectangle = Rectangle(4, 5)
rectangle.print_area()
