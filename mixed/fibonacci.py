# here n is the koto tomo porjonto ber korte cai
def fibonacci(n):
    f0=0
    f1=1
    i=3
    print(f0,f1,end=" ")
    while i<=n:
        fib = f0+f1
        print(fib,end=" ")
        f0= f1
        f1=fib
    
        i=i+1
    
    
fibonacci(50)