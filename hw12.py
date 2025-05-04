#Python program to find N largest elements from a list
l=input("Enter List Elements:").split()
n=int(input("Enter Value of n:"))
l.sort(reverse=True)
print("{} Largest Elements in the List:{}".format(n,l[:n]))