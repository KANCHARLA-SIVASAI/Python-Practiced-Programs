#Python program to print all negative numbers in a range
n=int(input("Enter Value of n:"))
if(n>0):
    res=list(range(-1,-(n+1),-1))
    print("All Negative Numbers upto {} ={}".format(-n,res))
else:
    print("Invalid Input")