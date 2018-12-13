class Rectangle:

    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2

    @property
    def width(self):

        '''rectagle height measured from top'''

        return self.x2 - self.y1

    @width.setter
    def width(self, value):

        self.x2 = self.x1 + value

    @property
    def height(self):

        '''rectangle height measured from top'''

        return self.y2 - self.y1

    @height.setter
    def height(self, value):

        self.y2 = self.y1 + value


class MyClass:

    r = Rectangle(10, 20, 30, 40)
    print(r.height, r.width)


m = MyClass()

