n = int(input())


if n>1:
    for i in range(2,n//2+1):
        if (n%i==0):
             print(f'{n} is not prime number')
             break
    else:
        print(f'{n} is prime number')
else:
    print((f'{n} is not a prime number'))

