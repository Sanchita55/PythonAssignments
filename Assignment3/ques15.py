# When interest compounds q times per year at an annual rate of r% for n years, the principle p compounds to an amount a as per the following formula. Write a program to read 10 sets of p, r, n & q and calculate the corresponding as.
# a = p(1+r/q)**np
for i in range(1,11):
    p = float(input('Enter principal: '))
    r = float(input('Enter rate: '))
    n = float(input('Enter time (in years): '))
    q = float(input('Enter compound interest: '))

    b = (1+r/q)**(n*q)
    a = p*b
    print(a, 'is the amount')