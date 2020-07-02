# To copy value from one list to another

# For LOOP

# list= [1,2,3,4,5,6,7,8,9,10]
# print(list)

# r=[]

# for i in list:
#    r.append(i)
# print(r) 

# # Using List Comprehension

# x=[i for i in list]
# print(x)

# to do square

# for i in list:
#     r.append(i*i)
# print(r)

# x=[i*i for i in list]
# print(x)

# # y=[]
# l= [1,2,3,4,5,6,7,8,9,10]

# res= map(lambda n: n*n,l)
# print(list(res))

# for i in y1:
#     print(i)


# num1 = [4, 5, 6]
# num2 = [5, 6, 7]

# result = map(lambda n1, n2: n1+n2, num1, num2)
# # print(result)
# # print(set(result))

# res= []
# for i in l:
#     if i%2 == 0:
#         res.append(i)
# print(res)

# lc= [i for i in l if i%2==0]
# print(lc)

# letter-no pair

pair= []

for i in 'abcd':
    for j in range(4):  
        pair.append((i,j))
print(pair)

res=[(ltr,num) for ltr in 'abcd' for num in range(4)]
print(res)


