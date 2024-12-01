import math
length = float(input('Enter the length of rectangle: '))
breadth = float(input('Enter the breadth of rectangle: '))
radius = float(input('Enter the radius of circle: '))

print('Area of Rectangle is ',length*breadth)
print('Perimeter of Rectangle is ',2*(length+breadth))
print('Area of Circle is ',math.pi*radius*radius)
print('Circumference of Circle is ',2*math.pi*radius)