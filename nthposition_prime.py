
count = 0
n = 2

while count <= 10:
    if n > 1:

        for i in range(2,n//2+1):
            if (n%i==0):
                break
        else:
            count += 1

            if count >= 6:
                print(n)
        n += 1
            
    
