target = 10
count = 0
n = 1

while count < target:
    summ = 0
    dummy = n
    for i in range(1,dummy//2+1):
        if (n %i ==0):
            summ += i
    if n == summ:
        print(n)
        count += 1
    n += 1
        
            
        
