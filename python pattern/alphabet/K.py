for line in range(7):
    for col in range(5):
        if col==0 or col+line==4 or line-col==2:
            print("* ",end="")
        else:
            print(end="  ")
    print()        
#  if col==0 or col+row==4 or row-col==2