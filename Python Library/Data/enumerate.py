l= ['bread','egg','butter','milk']

enu_g= enumerate(l)
print(enu_g)
print(type(enu_g))

print(list(enu_g))

enu_counter= enumerate(l,2)
print()
print(list(enu_counter))

# looping in 3 different ways

for n in enumerate(l):
    print(n)

for i,item in enumerate(l):
    print(i,item)

for count,item in enumerate(l,100):
    print(count,item)