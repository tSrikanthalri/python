a = int(input('enter the number a : '))
b = int(input('enter the number b :'))
c = int(input('enter the number c :'))


if (a>b) and (a>c):
    print(f'{a} is greater than {b} and {c}')
elif (b>a) and (b>c):
    print(f'{b} is greater than a and c')
else:
    print(f'{c} is greater than a and b')
