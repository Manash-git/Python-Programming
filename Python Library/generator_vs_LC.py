my_lits=[x*x for x in [1,2,3,4,5]]
print(my_lits)

my_gen=(y*y for y in [1,2,3,4,5])
# print(my_gen)
print(list(my_gen))