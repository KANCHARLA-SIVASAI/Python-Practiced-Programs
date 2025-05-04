l1=input("Enter Elements of 1st list:").split()
l2=input("Enter Elements of 2nd list:").split()
res=False
for ele in l1:
    if ele in l2:
        res=True
        break
print(res)