#input [10,20,30,40]
#output [20,10,40,30]

L= [10,20,30,40]

for ip in range(0,len(L),2):
    L[ip],L[ip+1] = L[ip+1],L[ip]
print(L)
