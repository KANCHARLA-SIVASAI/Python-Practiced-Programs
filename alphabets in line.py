#4.Write a python program which will accept a line of text and get only alphabets.
line=input("Enter A Line Of Text:")
if(line.isspace()):
    print("Space is Inavlid")
else:
    r=''
    for i in line:
        if(i.isalpha()):
            r=r+i
    print("Only Alphabests:",r)