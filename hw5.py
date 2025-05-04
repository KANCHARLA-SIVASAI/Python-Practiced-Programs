#Different ways to clear a list in Python
l=input("Enter List Elements:").split()
print("List of Elements:",l)
#logic1 using clear()
l.clear()
print("After Clearing list using logic1:",l)
#logic2 using assignment
l=input("Enter List Elements:").split()
print("List of Elements:",l)
l=[]
print("After Clearing list using logic2:",l)
#logic3 using del keyword
l=input("Enter List Elements:").split()
print("List of Elements:",l)
del l[:]
print("After Clearing list using logic3:",l)



