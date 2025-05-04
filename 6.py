l=[]
n=int(input("Enter no.of tuples in list:"))
for i in range(n):
    tup=tuple(map(int,input(f"Enter Tuple{i+1} Elements:").split()))
    l.append(tup)
print("Given List of tuples:",l)
for i in range(n):
    for j in range(i+1,n):
        if(l[i][-1]>l[j][-1]):
            l[i],l[j]=l[j],l[i]
print("result:",l)