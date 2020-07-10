def holo5(n):
    for line in range(0,n):
        for col in range(0,n):
            if (line+col==2 or line+col==6 or line-col==2 or col-line==2):
                print("*",end="")
            else:
                print(end=" ")
        print()


holo5(5)
print()
def holo7(n):
    for line in range(0,n):
        for col in range(0,n):
            if (line+col==3 or line+col==9 or line-col==3 or col-line==3):
                print("*",end="")
            else:
                print(end=" ")
        print()

holo7(7)
     