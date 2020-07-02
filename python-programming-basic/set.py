s1= {10,"Hello",2.5,"Python",10,'Hello',90}
print(type(s1))
print(s1)

l= [10,20,"lol",15.5]
s2= set(l)
print(s2)

s2.add("Hello")
print(s2)

# s2.add("Hello")
# print(s2)

s2.remove(20)
print(s2)

print(len(s1),len(s2))

s3= s1 & s2
print(s3)

s4= s1 | s2
print(s4)

print(s1 & s2)

print('Hello' in s1)
print('Hello' not in s1)

print(s1-s2)
print(s2-s1)

for i in s1:
    print(i)