
time=float(input('Enter the time taken by the worker to complete a job: '))
if time>=2 and time<=3:
    print('The worker is highly efficient')
elif time>3 and time<=4:
    print('The worker needs to improve speed')
elif time>4 and time<=5:
    print('The worker will be given training to improve the speed')
else:
    print('Sorry, the worker has to leave the company')