amount=int(input('Enter the amount to be withdrawn: '))
nohun=amount//100
amount=amount%100
nofifty=amount//50
amount=amount%50
noten=amount//10
amount=amount%10

print('No. of hundreds: ',nohun)
print('No. of fifties: ',nofifty)
print('No. of tens: ',noten)
