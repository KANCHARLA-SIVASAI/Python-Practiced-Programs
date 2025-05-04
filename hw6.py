#Python | Reversing a List
l=input("Enter List Elements:").split()
print("List Elements are:",l)
#logic1
l.reverse()
print("List Elements After Reversing using logic1:",l)
#logic2
l=l[::-1]
print("List Elements After Reversing using logic2:",l)
#logic3
reverse=list(reversed(l))
print("List Elements After Reversing using logic3:",reverse)


