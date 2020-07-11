def amrst(n):
    text= str(n)
    length=len(text)
    res=0
    if (length==2):
        print("Not Armstrong no.")
    else:
        for i in range(length):
            res= res+(int(text[i])**length)
        print(res)
        if n==res: 
            print("Armstrong no")
        else:
            print("Not Armstrong no.")
amrst(371)
amrst(1634)
amrst(54748)
amrst(155)

          
            