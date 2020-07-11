def hrt(n):
    for line in range(1,n+1):
        for col in range(1,n+1):
            if line==1 or col==n or col==line:
                print("* ",end="")
            else:
                print(end="  ")
        print()
        
hrt(10)