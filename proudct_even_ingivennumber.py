n = int(input('enter the number'))

product = 1

dummy = n
while dummy >0:
    rem = dummy%10

    if rem%2 ==0:
        product *= rem

    dummy //=10

print(product)
    
