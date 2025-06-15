n = int(input('enter the number'))

len_n = len(str(n))

arm_strong = 0
dummy = n

while dummy > 0:
    rem = dummy%10

    arm_strong += rem ** len_n

    dummy //= 10

    
print(arm_strong)

if n == arm_strong:
    print('Armstrong number')
else:
    print('Not Armstrong number')
