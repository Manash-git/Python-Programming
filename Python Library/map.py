def add(n):
    return n+n

# no=(1,2,3,4,5)
no=[1,2,3,4,5]
result=map(add,no)
# print(result)
# print(set(result))
print(list(result))

result1= map(lambda n: n+n, no)
# print(result1)
print(list(result1))

l1=[1,2,3,4]
l2=[5,6,7,8]

res=map(lambda x,y: x+y,l1,l2)
# print(res)
print(list(res))


text= ["Bat","cat","Dog"]
print(list(map(list,text)))


