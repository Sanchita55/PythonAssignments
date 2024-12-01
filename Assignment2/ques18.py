health=int(input('Enter your health condition(exc=1,poor=0): '))
age=int(input('Enter your age: '))
residance=int(input('Enter your residance place(city=1,village=0): '))
gender=input('Enter your gender(m,f): ')

if health==1 and age>=25 and age<=35 and residance==1 and gender=='m':
    print('Premium is Rs. 4 per thousand and your policy amount cannot exceed Rs. 2 lakhs!')
elif health==1 and (age>=25 and age<=35) and residance==1 and gender=='f':
    print('Premium is Rs. 3 per thousand and your policy amount cannot exceed Rs. 1 lakh!')
elif health==0 and (age>=25 and age<=35) and residance==0 and gender=='m':
    print('Premium is Rs. 6 per thousand and your policy amount cannot exceed Rs. 10000!')
else:
    print('You are not insured!!')