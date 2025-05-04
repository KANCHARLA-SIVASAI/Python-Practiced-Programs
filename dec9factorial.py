#write a python program which will calculate the factorial with following n*(n-1)*....*1*0!
n=int(input("Enter Number To Calculate Factorial:"))
if(n<0):
    print("Factorial Is Not Defined For Negative Numbers.")
else:
    r=1
    num=n
    while(num>0):
        r=r*num
        num=num-1
    print("The Factorial of {} is: {}".format(n,r))