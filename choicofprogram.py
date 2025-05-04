#write a python program which will display course name and on selctic a chaoice display that statement
print("="*50)
print("\t"*4,"Course Names")
print("="*50)
print("\t\t1.C")
print("\t\t2.C++")
print("\t\t3.Python")
print("\t\t4.Java")
print("="*50)
c=input("Enter Ur Choice:")
if(c.upper() == "C"):
    print("C Developed by Dennis Ritchie")
if(c.upper() == "C++"):
    print("C++ Developed by Bjarne Stroustrup")
if(c.upper() == "PYTHON"):
    print("Python Developed by Guido Van Rossum")
if(c.upper() == "JAVA"):
    print("Java Developed by James Goslin")




