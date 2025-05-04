#Write a python program which will display n perfect numbers and it must accepted from keyboard and it should be positive
num=int(input("Enter Number of Perfect Numbers:"))
res=[]
i=1
c=0
while(True):
    sum=0
    j=1
    while(j<(i//2+1)):
        if(i%j==0):
            sum=sum+j
        j=j+1
    if(sum==i):
        res.append(i)
        c=c+1
    if(c==num):
        break
    i=i+1
print("{} Perfect Numbers are: {}".format(num,res))
