#years to months,days
y=int(input("enter no.of years:"))
print("no.of months in {}years= {}".format(y,y*12))
print("no.of days in {}years= {}".format(y,y*365))

#months to years,days
m=int(input("enter no.of months:"))
print("no.of years=",m/12)
print("no.of days in {}months= {}".format(m,m*30))
#days to years,months
d=int(input("enter no.of days:"))
print("no.of years=",d/365)
print("no.of months for {}days= {}".format(d,d/30))

