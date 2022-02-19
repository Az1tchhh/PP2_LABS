class Student:
    def __init__(self, name):
        self.name = name
    def get_string(self):
        print (self.name.upper())
s = Student(input())
s.get_string()