#Calculate the day on 1st January of any year

year = int(input('Enter the year: '))
basic_year = 1900
year = (year-1)-basic_year

leap_year = year//4
remaining_year = year - leap_year
total_days = (remaining_year*365)+(leap_year*366)+1
     
firstday=total_days%7

if firstday==0:    
    print('Monday')
if firstday==1:    
    print('Tuesday')
if firstday==2:    
    print('Wednesday')
if firstday==3:   
    print('Thursday')
if firstday==4:    
    print('Friday')
if firstday==5:    
    print('Saturday')
if firstday==6:    
    print('Sunday')

