

with open('text.txt','w') as f:
    f.write("Hello World\n")
    
# Equivalent of this code is

eq_f = open("text.txt",'a')
try:
    eq_f.write("Equiavalent code\n")
finally:
    eq_f.close()
    

# If i write in a normal way

norm_f= open("text.txt",'a')
norm_f.write("Normal Code\n")
norm_f.close()
