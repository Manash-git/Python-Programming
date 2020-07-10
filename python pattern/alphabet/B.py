for line in range(7):
    for col in range(5):
        if (col==0) or ((line==0 or line==3 or line==6)and (col>0 and col<4)) or (col==4 and (line>0 and line<6 and line!=3)):
            print("* ",end="")
        else:
            print(end="  ")
    print()
            