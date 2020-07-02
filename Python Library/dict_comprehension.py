# zip example

name=["Bruce","Clark","Peter","Logan"]
heros=["Batman","Superman","Spiderman","Worlverine"]

# print(list(zip((name,heros))))

# for Loop

d={}
for x,y in zip(name,heros):
    d[x]=y

print(d)

# Dictionary comprehension

dc ={x:y for x,y in zip(name,heros)}
print(dc)

#  little bit advance

# dc_advance={n:h for n,h in zip(name,heros) if name!= "Peter"}
dc_advance={n:h for n,h in zip(name,heros) if n!= "Peter"}
print(dc_advance)