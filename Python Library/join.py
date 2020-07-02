
list1=['1','2','3','4']
s='-'

r= s.join(list1)
print(r)

list1=[1,2,3,4]
r= s.join(str(list1))
# print(r)

ch=['a','b','c','d']
print("".join(ch))
print("#".join(ch))
print("  ".join(ch))


t1='abc'
t2='123'

print("=> ",t1.join(t2))
print("=> ",t2.join(t1))

s= {'Python','C','Java'}
print(" -> -> ".join(s))

dc= {"Math":105,
     "Biology":208
     }
print(" -> ".join(dc))