def gcd(n1,n2):
    temp=min(n1,n2)
    
    while temp>0:
        if n1%temp==0 and n2%temp==0:
            print(f"GCD of {n1} and {n2} is => {temp}") 
            break
        else:
            temp-=1

gcd(4,2)

import math
print(math.gcd(4,2))