#Python program to find Sum of number digits in List
l=list(map(int,input("Enter Elements of List:").split()))
res=[]
for num in l:
    sum=0
    while(num>0):
        r=num%10
        sum=sum+r
        num=num//10
    res.append(sum)
print("Sum of Sum of number digits:",res)