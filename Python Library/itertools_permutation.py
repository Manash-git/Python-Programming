import itertools

horses=[1,2,3,4]

races= itertools.permutations(horses)
print(races)
# print(list(races))

# For for loop iteration
for i in races:
    print(i)
    
# print(races)

print(list(races))

# For return a list
print(list(itertools.permutations(horses)))