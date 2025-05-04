#Python program to print positive numbers in a list
l=input("Enter List Elements:").split()
res=[]
for x in l:
    if(float(x)>0):
        res.append(x)
print("All Positive Numbers={}".format(res))