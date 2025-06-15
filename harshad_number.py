n = int(input('enter the number'))

har = 0

dummy = n
while dummy > 0:
    rem = dummy%10
    har += rem

    dummy //=10

if n%har==0:
    print('harshad number')
else:
    print('not harshad number')



