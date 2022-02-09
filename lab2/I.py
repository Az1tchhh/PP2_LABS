discs = []
taken = []
for i in range(int(input())):
    a = input().split()
    if a[0] == '1': 
        discs.append(a[1])
    else:
        taken.append(discs[0])
        del discs[0]
    a=""
print(*taken)