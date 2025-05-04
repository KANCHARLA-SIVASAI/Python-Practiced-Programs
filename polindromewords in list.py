#write a python program which will accept list of words and from that words get only polindrom words
print("*"*50)
n=int(input("Enter no.of words in list:"))
if(n<=0):
    print("{} is invalid input".format(n))
    print("*" * 50)
else:
    lst = []
    for i in range(1, n + 1):
        s = input("enter word number{}:".format(i))
        if(s.isspace()):
            print("Spaces Are Not Allowed!")
            print("*" * 50)
        else:
             lst.append(s)
    if(len(lst)>0):
        print("*" * 50)
        print("List Of Words:", lst)
        print("*" * 50)
        res = []
        for word in lst:
            if (word == word[::-1]):
                res.append(word)
        else:
            if (len(res) != 0):
                print("list Of Polindrom Words:", res)
            else:
                print("There No Polindrom Words Existing In The List")
            print("*" * 50)




