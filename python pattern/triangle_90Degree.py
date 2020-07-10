
print(list(range(1,5+1)))
print()

def pattern(n):
    for line in range(1,n+1):
        # print(line)
        for space in range(line+1,n+1):
            print("  ",end="")
        for star in range(0,line):
            print("# ",end="")
        print("")
    for line in range(1,n):
        for space in range(0,line):
            print("  ",end="")
        for star in range(line,n):
            print("* ",end="")
        print("")
         
        
pattern(10)
         
         
     