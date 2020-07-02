#Use "b" to convert the number into binary format

# txt = "The binary version of {0} is {0:b}"
# print(txt.format(5))
# print(type(txt.format(5)))

# print(bin(5))
# print(type(bin(5)))

# x= bin(8)
# print(x)
# print(int(0b10111))
# print(type(int(0b10111)))
# # print(int(x))

# print("\n\n\n")
# # print(' '.join(format(5,'b')))

# print(type(''.join(format(5,'b'))))
# binary_convt= ''.join(format(5,'b'))

# print(type(binary_convt))
# covt= eval(binary_convt)
# covt= eval(binary_convt)
# print(type(covt))
# print(covt)
# print(bin(covt))




# Python3 code to demonstrate working of 
# # Converting String to binary 
# # Using join() + ord() + format() 

# # initializing string 
test_str ="GeeksforGeeks"

# # printing original string 
print("The original string is : ",test_str) 
print("The original string is : " +str(test_str)) 

# # using join() + ord() + format() 
# # Converting String to binary 
# res = ''.join(format(ord(i), 'b') for i in test_str) 
format_test= ''.join(format(i,'2') for i in test_str)
print(format_test)

covt_ascii= ''.join(format(ord(i),'<4') for i in test_str)
print(covt_ascii)

print("\n\n")
for i in test_str:
    # print(i + " => %i and binary is => %s" %(ord(i),bin(ord(i))))
    print(i + "  => {0:4}  and binary is => {1:>12}".format(ord(i),bin(ord(i))))
    
covt_bin= ''.join(format(ord(i),'b') for i in test_str)

# # printing result 
print("\nThe string after binary conversion : " + str(covt_bin)) 
print(type(covt_bin))
print("\nThe string after binary conversion : ",covt_bin)

print() 
