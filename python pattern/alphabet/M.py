for line in range(7):
    for col in range(7):
        if (col==0 or col==6) or (col==line and (col>0 and col<4)) or (col+line==6 and (col==4 or col==5)):
            print("* ",end="")
        else:
            print(end="  ")
    print()
    