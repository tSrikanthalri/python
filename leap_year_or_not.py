year = int(input('enter the year'))

if (year%100 !=0 and year%4==0 ) or (year%100 == 0 and year%400 == 0):
    print('LEAP YEAR')
else:
    print('NOT A LEAP YEAR')
    
