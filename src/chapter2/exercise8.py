import math
c = float(input("Enter initial amount"))
r = float(input("Enter the rate"))
n = float(input("Number of times the intrest is compounded"))
t = float(input("Number of year till maturation"))


tn = (t*n)
rn = (r/n)
p = (c*(1+rn)**tn)
#two_dec = "{0:.2f}".format(p)
#print(p)
print("%.2f" % p)
