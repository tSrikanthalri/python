'''n = int(input())

disarium = 0

len_n = len(str(n))

dummy = n
while dummy>0:
    rem = dummy %10
    disarium += rem ** len_n

    dummy //= 10
    len_n -= 1
if n == disarium:
    print('disarium')
else:
    print('not')'''



n = int(input())
summ = 0 

len_n = len(str(n))
dummy = n 
while dummy >0:
    rem = dummy %10
    summ += rem ** len_n
    dummy //= 10
    len_n -= 1 

if summ == n:
    print(n)
else:
    print("not")
 


    
