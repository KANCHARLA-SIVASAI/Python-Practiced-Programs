#employee pay-slip
eno=int(input("Enter Employee Number:"))
ename=input("Enter Employee Name:")
basicsal=float(input("Enter Employee Basic Salary:"))
if(basicsal<=0):
    print("{} is Invalid salary".format(basicsal))

if(basicsal>0):
    if (basicsal >= 10000):
        da = basicsal * (20 / 100)
        ta = basicsal * (10 / 100)
        hra = basicsal * (7 / 100)
        cca = basicsal * (0.5 / 100)
        ma = basicsal * (0.25 / 100)
        lic = basicsal * (2 / 100)
        gpf = basicsal * (1 / 100)
    if (basicsal < 10000):
        da = basicsal * (15 / 100)
        ta = basicsal * (7.5 / 100)
        hra = basicsal * (5 / 100)
        cca = basicsal * (0.25 / 100)
        ma = basicsal * (0.12 / 100)
        lic = basicsal * (1.5 / 100)
        gpf = basicsal * (1 / 100)
    netsal = (basicsal + ta + da + hra + cca + ma) - (lic + gpf)
    print("-" * 70)
    print("\tEMPLOYEE PAY SLIP")
    print("-" * 70)
    print("\tEMPLOYEE NUMBER: {}".format(eno))
    print("\tEMPLOYEE NAME: {}".format(ename))
    print("\tEmployee Basic Salary: {}".format(basicsal))
    print("\tDa: {}".format(da))
    print("\tTa: {}".format(ta))
    print("\tHra: {}".format(hra))
    print("\tCca: {}".format(cca))
    print("\tMa: {}".format(ma))
    print("\tLic: {}".format(lic))
    print("\tGpf : {}".format(gpf))
    print("\tNet Salary: {}".format(netsal))



