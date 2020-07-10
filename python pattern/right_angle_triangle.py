def r_a_t(n):
    for line in range(1,n+1):
        for star in range(1,line+1):
            print("* ",end="")
        print()

r_a_t(10)
print()

def r_a_t_1(n):
    for i in range(1,n+1):
	    print('* ' * i)
	    
r_a_t_1(10)

print()

print(["* "*i for i in range(1,6)])
