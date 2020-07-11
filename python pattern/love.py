for line in range(6):
    for col in range(7):
        if (line==0 and col%3!=0) or (line==1 and col%3==0) or (line+col ==8) or (line-col==2):
            print("* ",end="")
        else:
            print(end="  ")
    print()
    