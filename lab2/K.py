string = str(input())
new_string = string.split()
set_of_new_string = {''}
new_new_string = []
for i in range(len(new_string)):
    x = new_string[i].rstrip(",.?!")
    set_of_new_string.add(x)

for i in set_of_new_string:
    new_new_string.append(i)
new_new_string.sort()
print(len(new_new_string)-1)
for i in range(len(new_new_string)):
    if i>0:
        print(new_new_string[i])
        #sdfs