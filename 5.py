l=input("Enter List Elements:").split()
c=0
for item in l:
    if(len(item)>2 and item[0]==item[-1]):
        c=c+1
print("count=",c)
