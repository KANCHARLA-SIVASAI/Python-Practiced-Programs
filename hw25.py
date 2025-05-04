#Python to Remove empty Tupples from List
l=[]
n=int(input("enter no.of Elements in List:"))
for i in range(n):
    list1=input(f"Enter Tuple{i+1} Elements:").split()
    tuple1=tuple(list1)
    l.append(tuple1)
print("List Elements Before Removing Empty Tuples= {}".format(l))
for sublist in l:
    if(len(sublist)==0):
        l.remove(sublist)
print("List Elements After Removing Empty Tuples= {}".format(l))