def f_tr(n):
    res=1
    for line in range(1,n+1):
        for col in range(0,line):
            print(res,end=" ")
            res+=1
        print()
        
f_tr(4)
        