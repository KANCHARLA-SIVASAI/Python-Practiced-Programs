#Python to Remove empty List from List
l=[]
n=int(input("enter no.of Elements in List:"))
for i in range(n):
    sublist=input(f"Enter sublist{i+1} Elements:").split()
    l.append(sublist)
print("List Elements Before Removing Empty Lists= {}".format(l))
for sublist in l:
    if(len(sublist)==0):
        l.remove(sublist)
print("List Elements After Removing Empty Lists= {}".format(l))