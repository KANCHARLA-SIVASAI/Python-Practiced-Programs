#Python program to find smallest number in a list
l=input("Enter List Elements:").split()
l.sort()
print("Smallest Element in the List:{}".format(l[0]))