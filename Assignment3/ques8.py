# Write a program to find the octal equivalent of the entered number.
'''oct = 0
rev = 0
num = int(input('Enter the number: '))
while num > 0:
    rem = num % 8
    oct = 10 * oct + rem
    num //= 8
while oct > 0:
    rem1 = oct % 10
    rev = rev * 10 + rem1
    oct //= 10
    print(rev,'is octal equivalent')    '''

decimal_num = int(input('Enter a decimal number: '))
octal_num = ''
while decimal_num > 0:
    octal_num = str(decimal_num % 8)
    decimal_num //= 8
print('The octal equivalent is:', octal_num)