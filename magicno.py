#8.write a python program which will accept a number and decide whether it is magic number or not
n=int(input("Enter A Number:"))
res=f'{n} is magic number' if str(n*n).endswith(str(n)) else f'{n} is not magic number'
print(res)