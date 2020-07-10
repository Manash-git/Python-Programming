def oddrat(n):
    for line in range(0,n):
        print("* " * ((2*line)+1))
    print()
    
oddrat(8)

def evenrat(n):
    for line in range(n):
        print("* "* (2*line))
evenrat(8)