'''n = int(input('enter the number'))

product = 1

i = 1
while i <= n:
    
    product *= i

    i += 1
    
print(product)
'''

n = int(input('enter the number'))

product = 1

dummy = n
while dummy >0:
    rem = dummy%10
    
    product *= rem

    dummy //=10

print(product)
    

