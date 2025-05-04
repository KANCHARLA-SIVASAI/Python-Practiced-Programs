#write a python program which will generate the odd numbers in reverse order within n
n=int(input("Enter How Many Range in which u want Odd Numbers:"))
if(n<=0):
    print("{} is Invalid Input:".format(n))
else:
    print("-"*50)
    print("List of Odd Numbers within {}".format(n))
    i=n
    while(i>0):
        if(i%2!=0):
            print(i)
        i=i-1
    else:
        print("-" * 50)