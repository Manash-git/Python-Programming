# data = [5,2,7,9,0]

# # Ascending Order sort
# a_sort= sorted(data)
# print(a_sort)

# # Descending Order sort

# d_sort= sorted(data,reverse=True)
# print(d_sort)



# text= ['abc','xyzb','a','ab','abcd']
# print(sorted(text,reverse=True))
# print(sorted(text,reverse=False))




# take the second element for sort
# def take_second(elem):
#     return elem[1]


# # random list
# random = [(2, 2), (3, 4), (4, 1), (1, 3)]

# # sort list with key
# sorted_list = sorted(random, key=take_second)

# # print list
# print('Sorted list:', sorted_list)

# Nested list of student's info in a Science Olympiad
# List elements: (Student's Name, Marks out of 100 , Age)
participant_list = [
    ('Alison', 50, 18),
    ('Terence', 75, 12),
    ('David', 75, 20),
    ('Jimmy', 90, 22),
    ('John', 45, 12)
]


def sort_format(n):
    rest= 100-n[1]
    return (rest,n[2])

sorted_pl= sorted(participant_list,key=sort_format)
print(sorted_pl)

print()

# Using Lambda function

sorted_pl_lambda= sorted(participant_list, key=lambda n:(100- n[1],n[2]))
print(sorted_pl_lambda)
