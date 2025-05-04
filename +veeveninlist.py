#2.write a python program which will accept list of numerical values and get only positive even values.
print("*" * 50)
n=int(input("Enter no.of values in list:"))
l=[]
if(n<=0):
    print("invalid input")
    print("*"*50)
else:
    for i in range(1,n+1):
        val=int(input("enter value{}:".format(i)))
        l.append(val)
    print("*"*50)
    print("Given Values Are:",l)
    print("*"*50)
    res=[]
    for i in l:
        if i>0 and i%2==0:
            res.append(i)
    print("All Positive Even Values Are:",res)
    print("*"*50)

