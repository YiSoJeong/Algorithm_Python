class Circle:
    def __init__(self, r):
        self.r = r

    def print_area(self):
        print('원의 면적: {:.2f}'.format(3.14*self.r*self.r))


circle = Circle(2)
circle.print_area()
