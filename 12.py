#logic1 using enumerate function
l=input("Enter Elements Of List:").split()
print("Elements of List Before Removing:")
l=[x for (i,x) in enumerate(l) if i not in (0,4,5)]
print("Elements of List After Removing 0th,4th,5th elements:",l)
#logic 2 using range function
l=input("Enter Elements Of List:").split()
print("Elements of List Before Removing:")
l=[l[i] for i in range(len(l)) if i not in (0,4,5)]
print("Elements of List After Removing 0th,4th,5th elements:",l)
