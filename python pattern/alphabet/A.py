for line in range(7):
    for col in range(5):
        if ((col==0 or col==4) and  line !=0) or ((line==0 or line==3) and col>0 and col<4):
            print("* ",end="")
        else:
            print(end="  ")
    print()
             