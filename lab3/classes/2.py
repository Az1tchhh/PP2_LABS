class Square:
    def __init__(self,length):
        self.length = length
    
class Shape(Square):
    def __init__(self, length):
        super().__init__(length)
    def Area(self):
        print(self.length**2)

a = Shape(int(input()))
a.Area()