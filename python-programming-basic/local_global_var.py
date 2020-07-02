
# Local Variable

# def abd():
#     k=5
#     print(k)

# def xyz():
#     k=8
#     print(k)
#     abd()
#     print(k)

# xyz()

# t=5 

# def global_var_1():
#     t=10
#     print(t)
    
# def global_var_2():
#     print(t)


# global_var_1()
# global_var_2()


# def my_add_G(b):
#     a=b+2
#     print(a)
#     return a

# a=10
# c=my_add_G(a)
# print(a)
# print(c)

def my_add_G(b):
    global a
    a=b+2
    print(a)
    return a

a=10
c=my_add_G(a)
print(a)
print(c)