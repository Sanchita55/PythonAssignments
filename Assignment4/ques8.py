# Write a program in Python to calculate combinatoric C(n,r) using function.
def fact(n):
    j = 1
    while n>0:
        j = j*n
        n = n-1
        return j
n = int(input('Enter the value of n: '))
r = int(input('Enter the value of r: '))
print('The value of C(n,r) is:',fact(n)//fact(r)*fact(n-r))
