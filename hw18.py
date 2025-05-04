#Python program to print negative numbers in a list
l=input("Enter List Elements:").split()
res=[]
for x in l:
    if(float(x)<0):
        res.append(x)
print("All Negative Numbers={}".format(res))