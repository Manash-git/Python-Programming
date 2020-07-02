
name=['Sakib','Priya','Pritom','Supty','Manash','Angshuman']

m= max(len(i) for i in name)

print(m)

for i in name:
    print(i.ljust(m+3,"-")+":")


for j in name:
    print(j.rjust(m+10,">"))

for x in name:
    print(x.center(m+5,"~"))
    
    
    