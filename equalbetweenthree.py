a = int(input('enter the number a : '))
b = int(input('enter the number b :'))
c = int(input('enter the number c :'))


if (a>b) and (a>c):
    print(f'{a} is greater than {b} and {c}')
elif (b>a) and (b>c):
    print(f'{b} is greater than {a} and {c}')
elif (c>a) and (c>b):
    print(f'{c} is greater than {a} and {b}')
elif (a==b)or (a>c):
    print(f'both a and b is equal and {a} is greater than c')
elif (a==c) or (a>b):
    print('both and c is equal and a is greater than b')
elif (a==b)or(b>c):
    print('both a and b is equal and b is greater than c')
elif (a==c) or (c>b):
    print('both and c is equal and  is greater than b')
else:
    print('ALL THREE NUMBERS ARE EQUAL')
