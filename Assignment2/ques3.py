yr = int(input('Enter a year: '))
if yr%100==0:
    if yr%400==0:
        print('Leap year')
    else:
        print('Not a Leap year')
else:
    if yr%4==0:
        print('Leap year')
    else:
        print('Not a leap year')