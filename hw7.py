#Python program to find sum of elements in list
l=input("Enter List Elements:").split()
sum=0
for x in l:
    sum=sum+float(x)
print("Sum Of Elements Of List:{}".format(sum))