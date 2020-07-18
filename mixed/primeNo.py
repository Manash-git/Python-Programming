def primeNo(n):
    flag=0
    if n>0:
        for i in range(2,n):
            if n%i == 0:
                flag=0
                break       
            else:
                flag=1
    print("Prime" if flag==1 else "Not prime")      # Ternary Operator
        
primeNo(-5)