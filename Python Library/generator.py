# Using for loop

def square(n):
    l=[]
    for i in n:
        l.append(i*i)
    return l

res= square([1,2,3,4,5])
print(res)

# using generator

def sqr_Gen(x):
    for i in x:
        yield i*i

res_Gen= sqr_Gen([1,2,3,4,5])
print(res_Gen)
print(type(res_Gen))

# print(next(res_Gen))
# print(next(res_Gen))
# print(next(res_Gen))
# print(next(res_Gen))
# print(next(res_Gen))


# for j in res_Gen:
#     print(j)

print(list(res_Gen))