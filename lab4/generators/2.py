N = int(input())

def numbers():
    i=1

    while(i<=N):
        if(i%2==0):
            yield i
        i+=1
a = []
for num in numbers():
    a.append(str(num))
print(", ".join(a))
'''
class numbers():
    def __iter__(self):
        self.a = 1
        return self
    def __next__(self):
        if(self.a<=N):
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration
n = numbers()
myiter = iter(n) 
for x in myiter:
    print(x)
'''
