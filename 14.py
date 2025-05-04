l=list(map(int,input("Enter List Elements:").split()))
print("List Elements After Removing Even Numbers:",l)
for x in l:
    if(x%2==0):
        l.remove(x)
print("List Elements After Removing Even Numbers:",l)