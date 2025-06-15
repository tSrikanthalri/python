n1 = int(input())
n2 = int(input())

dummy = n1

while dummy <= n2:
    num = dummy 
    
    sum_factorial = 0
    while num > 0:
        rem = num % 10
        
        factorial = 1
        i = 1 
        while i <= rem:
            factorial *= i 
            
            i += 1
        sum_factorial += factorial
        num //= 10
    if dummy == sum_factorial:
        print(f'{dummy} is a super')
        
    dummy +=  1
        
