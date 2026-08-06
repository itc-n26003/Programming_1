class Rectangle:
    '''長方形'''
    angle = 90

    def __init__(self, width, height):
        self.name = 'rectangle'
        self.widht = width
        self.height = height
        self.perimeter = self.calc_perimeter()
        self.area = self.calc_area()

    def calc_perimeter(self):
        w = self.widht
        h = self.height
        return (w + h) * 2

    def calc_area(self):
        w = self.widht
        h = self.height
        return w * h

    def show_attributes(self):
        ang = self.angle
        n = self.name
        w = self.widht
        h = self.height
        p = self.perimeter
        a = self.area
        print("name: {}, widht: {}, height: {}, angle: {}".format(n, w, h, ang))
        print("perimeter: {}, area: {}".format(p, a))

## インスタントを使って実行
#r1 = Rectangle(4, 3)
#r1.show_attributes()

class Square(Rectangle):
    '''正方形'''

    def __init__(self, width):
        super().__init__(width, width)
        self.name = 'square'

# インスタントを作って実行
s1 = Square(4)
s1.show_attributes()
