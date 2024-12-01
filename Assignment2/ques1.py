cp = float(input('Enter cost price: '))
sp = float(input('Enter selling price: '))
p = sp-cp
l = cp-sp
if p>0:
    print('The seller made a profit of Rs. ',p)
if l>0:
    print('The seller incurred loss of Rs. ',l)
if p==0:
    print('There is no loss, no profit')