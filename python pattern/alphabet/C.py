for line in range(7):
    for col in range(5):
        if (col==0 and (line!=0 and line!=6)) or (col>0 and (line==0 or line==6)):
            print("* ",end="")
        else:
            print(end=" ")
    print() 
    