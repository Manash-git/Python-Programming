def nothing():
    pass
nothing()

def my_func():
    print("Hello Python")
    
my_func()

def my_add(n):
    add= n +5
    return add


res=my_add(7)
print(res)

def my_mul(a,b):
    # mul= a*b
    # return mul
    return a*b

print(my_mul(2,10))
print(my_mul(9,"love"))

def mul_sum(*n):
    sum = 0
    for i in n:
        sum=sum+i
    return sum

print(mul_sum(5))
print(mul_sum(5,5))
print(mul_sum(5,5,15,30,100))

