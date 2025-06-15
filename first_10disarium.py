target = int(input('enter the position'))
count = 0
n = 1

while count <= target:
    summ = 0
    len_n = len(str(n))
    dummy = n
    while dummy > 0:
        rem = dummy % 10
        summ += rem ** len_n

        len_n -= 1
        dummy //= 10
    if summ == n:
        count += 1
        if count == target:
            print(n)
    n += 1

'''
target = 10 
count = 0 
n = 1

while count <= target:
    summ = 0
    len_n = len(str(n))
    dummy = n 
    while dummy > 0:
        rem = dummy % 10 
        summ += rem ** len_n
        
        len_n -= 1
        dummy //= 10
    if summ == n:
        print(n)
        count += 1 
    n += 1 '''
        
        
