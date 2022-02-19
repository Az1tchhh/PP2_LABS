class Square:
    def __init__(self,length):
        self.length = length
    
class Shape(Square):
    def __init__(self, length):
        super().__init__(length)
    def Area(self):
        print(self.length**2)
class Rectangle(Shape):
    def __init__(self , length, width):
        self.length = length
        self.width = width
    def Area(self):
        print(self.length*self.width)
n1 = int(input())
n2 = int(input())
a = Rectangle(n1,n2)
a.Area()