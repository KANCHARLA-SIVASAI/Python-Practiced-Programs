#Python program to print all positive numbers in a range
n=int(input("Enter Value of n:"))
if(n>0):
    res=list(range(1,n+1))
    print("All Positive Numbers upto {} ={}".format(n,res))
else:
    print("Invalid Input")