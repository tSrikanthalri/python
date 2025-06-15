target = int(input('enter the target : '))
count = 0 
n = 2 

while count < target:
        if n > 1:
            for i in range(2,n//2+1):
                if (n%i==0):
                    break 
            else:
                print(n)
                count += 1
            n += 1
