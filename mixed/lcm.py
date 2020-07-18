def lcm(n1,n2):
    max_no= max(n1,n2)
    min_no= min(n1,n2)
    # print(max_no,min_no)
    mul_table=max_no
    while True:
        if mul_table% min_no == 0:
            print(f"LCM of {n1} and {n2} is => {mul_table}")
            break
        else:
            mul_table= mul_table+max_no
            print(max_no)
            

lcm(4,9)
lcm(4,3)
lcm(6,3)

# print(min(9,6))