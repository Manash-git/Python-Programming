# Normal Way

def fact(n):
    f=1
    for i in range(1,n+1):
        f=f*i
    print("Factorial of %i => %i"%(n,f))

fact(4)

# Recursion function

def recursion_fact(n):
    if n==0:
        return 1
    else:
        return n * recursion_fact(n-1)
    
x= recursion_fact(4)
print(x)

a=5
print("Resursion Factorial of %i => %i"%(a,recursion_fact(a)))

