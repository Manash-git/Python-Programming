l= [10,21,2,53,6,100,80,35]
# n=int(input("Enter Key: "))

#  Break Example

# for i in l:
#     print(i,n)
#     if i==n:
#       print("\n  Found\n")
#       break

# Continue Example

# for j in l:
#     if j%2!=0:
#         continue
#     print(j)

for j in l:
    if j%2==1:
        continue
    print(j)
