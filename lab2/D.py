size = int(input())
if(size%2==0):
    for i in range(size):
        for j in range(size):
            string =""
            string ="#"*(i+1)+"."*(size-i-1)
        print(string)
else:
    for i in range(size):
        for j in range(size):
            string =""
            string ="."*(size-i-1)+"#"*(i+1)
        print(string)