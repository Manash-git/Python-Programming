# if the gcd of two number is 1, then it is called Co-Prime Number
import math
def coPrime(n1,n2):
    if math.gcd(n1,n2)==1:
        print("Co-prime Number")
    else:
        print("Non Co-Prime number")

coPrime(5,10)