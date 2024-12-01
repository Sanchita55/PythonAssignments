l = int(int(input('Enter the length of rectangle: ')))
b = int(input('Enter the breadth of rectangle: '))
area = l*b
peri = 2*(l+b)
if area>peri:
    print('Area is greater than perimeter')
else:
    print('Area is not greater than perimeter')