def binary_Con(n):
    bits=[]
    while n>0:
        # bits.append(n%2)
        bits.append(str(n%2))
        n = n//2
    
    bits.reverse()
    print(bits)
    print("".join(bits))

# print(binaryConversion(10))
binary_Con(10)