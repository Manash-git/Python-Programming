def diamond(n):
    for line in range(1,n+1):
        print(" "*(n-line)+"* "*line)
    for line in range(n-1):
        print(" "*(line+1)+ "* "*((n-1)-line))
         
diamond(15)
