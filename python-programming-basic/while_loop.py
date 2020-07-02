n = int(input("Enter number: "))

# print("Print value from 1 to ",n)

# i=1
# while i<=n:
#     print("=> ",i)
#     i+=1
# print("\nEnd of Prog.")

print("Multiplication table of ",n)

i=1
while i<=10:
    # print("=> ",i*n)
    print("%i * %i => %i"%(n,i,n*i))
    i+=1

print("\nEnd")