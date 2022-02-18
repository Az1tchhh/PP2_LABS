class Student:
    def init(self,name):
        self.name=name
    def get_string(self):
        return self.name
s1 = Student('az')
print(s1.get_string())