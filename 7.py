l=input("Enter List Elements:").split()
uniquelist=[]
for x in l:
    if x not in uniquelist:
        uniquelist.append(x)
l=uniquelist
print("After Removing Duplicates From list :",l)
