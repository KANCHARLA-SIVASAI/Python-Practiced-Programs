#Python program to swap two elements in a list
l=list(map(float,input("\t\tEnter List Elements:").split()))
i,j=int(input("\t\tEnter index of first element to swap:")),int(input("\t\tEnter index of second element to swap:"))
l[i],l[j]=l[j],l[i]
print(f"\t\tList of Elements After Swaping Element{i},Element{j}",l)