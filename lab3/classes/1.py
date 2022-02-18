class Student:
    def init(self,name):
        self.name=name
    def get_string(self):
        return self.name
s = Student('az')
print(s.get_string())