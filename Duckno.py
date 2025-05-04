#7.write a python program which will accept any numerical integer value and decide whether it is duck number or not?
print("*"*50)
s=input("Enter a positive integer value:")
if(s[0]=='0' or '0' not in s):
    print("{} is Not Duck Number".format(s))
    print("*" * 50)
else:
    print("{} is Duck Number".format(s))
    print("*" * 50)






