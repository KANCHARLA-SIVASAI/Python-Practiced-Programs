#Python program to Sort the values of first list using second list
l1=input("Enter Elements of list1:").split()
l2=list(map(int,input("Enter Elements of list2:").split()))#indices
l3=list(set(l2))#unique values of indices
l3.sort()
res=[]
for i in l3:
    for j in range(0,len(l2)):
        if(l2[j]==i):
            res.append(l1[j])
print(res)