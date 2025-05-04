#3.write a python program which will accept list of numerical values and find the sum of positive numerical values and also find seperately negative values sum
print("*" * 50)
n=int(input("Enter no.of values in list:"))
l=[]
if(n<=0):
    print("invalid input")
    print("*"*50)
else:
    for i in range(1,n+1):
        val=float(input("enter value{}:".format(i)))
        l.append(val)
    print("*"*50)
    print("Given Values Are:",l)
    print("*"*50)
    ns,ps=0,0
    for i in l:
        if i>0:
            ps=ps+i
        if i<0:
            ns=ns+i
    print("Sum Of All Positive Values Are:",ps)
    print("Sum Of All Negative Values Are:",ns)
    print("*"*50)

