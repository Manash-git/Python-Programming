l=[0,0,1,2,2,3,4,5,5,6,6,6,6,7,8,9,10]
print(set(l))

# for loop

s1=set()
for i in l:
    s1.add(i)
    
print(s1)

# Using Set Comprehension

sc = {n for n in l}
print(sc)