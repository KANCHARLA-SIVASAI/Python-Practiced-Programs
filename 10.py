l=input("Enter List of Words:").split()
n=int(input("Enter Value of n:"))
res=[]
for x in l:
    if(len(x)>n):
        res.append(x)
print(f"Words Those are longer than {n} are {res}")