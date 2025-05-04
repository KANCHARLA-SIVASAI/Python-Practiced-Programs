#write a python program which will generate the odd numbers within n
n=int(input("Enter How Many Range in which u want Odd Numbers:"))
if(n<=0):
    print("{} is Invalid Input:".format(n))
else:
    print("-"*50)
    print("List of Odd Numbers within {}".format(n))
    odd=1
    while(odd<=n):
        print(odd)
        odd=odd+2
    else:
        print("-" * 50)