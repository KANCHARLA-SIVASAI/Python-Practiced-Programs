#Multiplication tables in a range
n=int(input("Enter How many mult tables you want:"))
print("-" * 50)
if(n<1):
    print("\t\t{} is invalid input".format(n))
    print("-" * 50)
else:
    for i in range(1,n+1):
        print("\t\t{} table:".format(i))
        for j in range(1,11):
            print("\t\t{} X {} = {}".format(i,j,i*j))
        print("-"*50)
