days = int(input('Enter the number of days: '))
if days>0 and days <=5:
    fine = 0.50 * days
if days>=6 and days<=10:
    fine = 1 * days
if days>10:
    fine = 5 * days
    if days>30:
        print('Your membership would be cancelled')
print('You have to pay the fine of Rs.',fine)