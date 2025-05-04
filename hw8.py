#Python Program to Multiply all numbers in the list
l=input("Enter List Elements:").split()
product=1
for x in l:
    product=product*int(x)
print("Product Of all Elements Of List:{}".format(product))