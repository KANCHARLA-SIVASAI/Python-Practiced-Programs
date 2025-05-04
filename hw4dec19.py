#Write a python program which will accept a line of text and obtain those words whose first letter and last letter is same
l=input("Enter a Line Of Text:").split()
if(len(l)==0):
    print("Please Enter A Line Of Text")
res=[]
for sublist in l:
    if(sublist[0]==sublist[-1]):
        res.append(sublist)
print("Words With First Letter And Last Letter is Same:",res)