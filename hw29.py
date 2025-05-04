#Break a list into chunks of size N in Python
l=input("Enter List Elements:").split()
n=int(input("Enter Size of chunk:"))
res=[]
for i in range(0,len(l),n):
    res.append(l[i:i+n])
print(res)