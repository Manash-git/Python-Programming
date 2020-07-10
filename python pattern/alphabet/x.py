for row in range(5):
    for col in range(5):
        if ((col==row)) or ((col+row==4)):
            print('*',end='')
        else:
            print(end=' ')
    print()

def x_pattern(n):
    if n%2==0:n+=1
    print(n)
    print()
    for row in range(n):
        for col in range(n):
            if (row==col or (row+col==n-1)):
                print("*", end="")
            else:
                print(end=" ")
        print()
print()
x_pattern(8)
    