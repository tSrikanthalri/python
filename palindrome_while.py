n = int(input('enter the number : '))

reverse = ''

dummy = n
while dummy>0:
    rem = dummy%10
    reverse += str(rem)

    dummy //= 10


print(reverse)
print(str(n))

if str(n) == reverse:
    print('Palindrome')
else:
    print('Not')
