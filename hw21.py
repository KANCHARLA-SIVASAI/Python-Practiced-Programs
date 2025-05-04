#Remove multiple elements from a list in Python
l=input("Enter List Elements:").split()
m=input("Enter Elements to Remove From List:").split()
for x in m:
    if x in l:
        l.remove(x)
print("Elements Of List After Removing {} = {}".format(m,l))