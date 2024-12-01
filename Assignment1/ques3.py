# Calculation of aggregate & percentage marks
sub1 = int(input('Enter the marks of sub1: '))
sub2 = int(input('Enter the marks of sub2: '))
sub3 = int(input('Enter the marks of sub3: '))
sub4 = int(input('Enter the marks of sub4: '))
sub5 = int(input('Enter the marks of sub5: '))

aggr = sub1 + sub2 + sub3 + sub4 + sub5
per = aggr/5

print('Aggregate Marks = ',aggr)
print('Percentage Marks = ',per)

