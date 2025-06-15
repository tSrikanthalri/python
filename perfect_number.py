n = int(input('enter the number'))

sum_divisors = 0

for i in range(1,n):
    if n%i==0:
        sum_divisors += i
if n == sum_divisors:
    print(n)
        
