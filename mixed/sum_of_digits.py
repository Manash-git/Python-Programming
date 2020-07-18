def sod_strConvertway(n):
    n= str(n)
    sod = 0
    
    for i in range(len(n)):
        sod= sod + int(n[i])
    print(f"Sum of {n} is {sod}")
    

n=129
# sod_strConvertway(n)

# print(str(n))
# print(type(str(n)))
# print(str(n)[2])
# print(type(n))

# mathmatical way

def sod_math_way(n):
    sod=0
    cache = n
    
    while n>0:
        temp = n%10
        sod= sod + temp
        n= n//10
    print(f"Sum of {cache} is => {sod}")

sod_math_way(12015)