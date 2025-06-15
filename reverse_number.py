n = int(input('enter the number : '))

reverse_n = ''

dummy = n
while dummy >0:
    rem = dummy%10
    reverse_n += str(rem)

    dummy //= 10
print(reverse_n)

'''n = int(input('enter the number : '))

reverse_n =0

dummy = n
while dummy >0:
    rem = dummy%10
    reverse_n = reverse_n*10 +rem

    dummy //= 10
print(reverse_n)'''


