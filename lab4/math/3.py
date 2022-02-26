import math
n = float(input("Input number of sides: "))
l = float(input("Input the length of a side: "))
alpha = (180-360/n)/2

h=l*math.tan(math.radians(alpha))/2
area = l*h/2*n
print("The area of the polygon is: ", round(area,3))