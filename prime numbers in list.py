#Write a python program which will accept list of numerical integer values and get prime numbers from that list
print("*"*70)
l=list(map(int,input("Enter Numerical Integers Seperated by Spaces:").split()))
print("\t\tPrime Numbers are:")
for num in l:
    if(num>1):
        c = 0
        for i in range(2, num):
            if (num % i == 0):
                c = c + 1
        if (c == 0):
            print("\t\t", num)

print("*"*70)
