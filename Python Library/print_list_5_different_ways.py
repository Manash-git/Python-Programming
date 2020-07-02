
a=[5,7,9,2,4]

# For Loop
# 1
for i in a:
    print(i)
    
# 2

for i in range(len(a)):
    print(a[i])

# without loop

print(a)
print(*a)
print(*a,sep=', ')
print(*a,sep='\n')

# Using join
a1= ["hello","world"]
print(" ".join(a1))

# Using slice
print(str(a)[1:-1])