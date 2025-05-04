#Python program to find Cumulative sum of a list
l=list(map(float,input("Enter Elements Of List:").split()))
cumulative_sum=[]
sum=0
for x in l:
    sum=sum+x
    cumulative_sum.append(sum)
print("Cumulative Sum:",cumulative_sum)