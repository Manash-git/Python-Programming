
l= [10,20,30,45]

print(l[3])

# try:
#     print(l[20])
# except IndexError as e:
#     print(e)

try:
    print(l[10])
except Exception as X:
    print(X)