# with open("date.txt",'a+') as f:
#     # f.write("Hello World\n")
#     f.seek(13,0)
#     print(f.read())
# # ("Test")

with open("date.txt",'r') as f:
    f.seek(13)
    print(f.tell())
    # print(f.readline())
    print(f.readline().encode('utf-8','strict'))
    # str1= f.readline()
    # print(str1.encode('utf-8'))
    
with open("date.txt",'rb') as f:
    f.seek(-3,2)
    # print(f.tell())
    # print(f.readline())
    # print(f.readline().decode('utf-8'))
    # print(str(f.readline()))

