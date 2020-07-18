def gcd(n1,n2):
    
    # Formula:  n1*n2 = LCM(n1,n2) * gcd (n1,n2)
    # so gcd = (n1*n2) / LCM (n1,n2)
    
    print(f"GCD of {n1} and {n2} is {(n1*n2)//lcm(n1,n2)}")

def lcm(n1,n2):
    max_no= max(n1,n2)
    min_no= min(n1,n2)
    # print(max_no,min_no)
    mul_table=max_no
    while True:
        if mul_table% min_no == 0:
            # print(f"LCM of {n1} and {n2} is => {mul_table}")
            return mul_table
        else:
            mul_table= mul_table+max_no
            # print(max_no)

gcd(5,2)