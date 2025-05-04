#write a python program which will find perfect numbers within 1000
res=[]
for n in range(1,1000):
    sum=0
    for i in range(1,n):
        if(n%i==0):
            sum=sum+i
    if(sum==n):
        res.append(n)
print("Perfect Numbers within 1000:",res)
