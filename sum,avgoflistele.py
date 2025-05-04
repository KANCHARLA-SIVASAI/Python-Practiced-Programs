#write a python program which will find sum and average of list of numbers
lst=list(map(int,input("Enter list elements:").split()))
s=0
print('*'*50)
print("List of values:")
sum=0
for val in lst:
    print("\t",val)
    sum=sum+val
else:
    print("*"*50)
    print("\tsum={}".format(sum))
    print("\tavg={}".format(sum/len(lst)))


