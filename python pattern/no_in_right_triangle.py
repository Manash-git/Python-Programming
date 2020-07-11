def rtr(n):
    for line in range(n,0,-1):
        print((str(line)+" ")*line)
    print()
    for line in range(n,0,-1):
        for col in range(line):
            print(col+1,end=" ")
        print()
rtr(5)
    