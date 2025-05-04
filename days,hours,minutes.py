#days to hours,mins
d=int(input("enter no.of days:"))
print("no.of hours in {}days= {}".format(d,d*24))
print("no.of mins in {}days= {}".format(d,d*24*60))
print("*"*50)
#hours to days,mins
h=int(input("enter no.of hours:"))
print("no.of days for {}hours= {}".format(h,h/24))
print("no.of mins in {}hours= {}".format(h,h*60))
print("*"*50)

#mins to hours,days
m=int(input("enter no.of mins:"))
print("no.of hours for {}mins= {}".format(m,m/60))
print("no.of days for {}mins= {}".format(m,m/(24*60)))

