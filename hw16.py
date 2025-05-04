#Python program to print all odd numbers in a range
n=int(input("Enter Value Of n:"))
res=[]
for i in range(1,n+1):
    if(i%2!=0):
        res.append(i)
print("Odd Numbers Upto {} = {}".format(n,res))