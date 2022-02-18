import math
def Volume(Raduis):
    return 4/3*math.pi*Raduis**3
radius = int(input())
print(Volume(radius))