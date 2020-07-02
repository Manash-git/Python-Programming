
from array import array

arr1=array('i',[2,4,6,8,10,12,14])  # Integer type array

print("DateType=> ",arr1.typecode)
print("each item memory allocation in Byte: ",arr1.itemsize)

# Manupulation

# arr1.insert(0,1)
# print(arr1)

# arr1.append(16)
# print(arr1)

# arr1.extend([20,22,24])
# print(arr1)
# print()

# for i,item in enumerate(arr1,100):
#     print(i,item)

print(arr1)


# for j,item in enumerate(arr1):
#     arr1[j]= item * 2

# print(arr1)

arr2=array('i')

# for j,item in enumerate(arr1):
#     # arr2.append(item*2)
#     arr2.insert(j,item+100)
    
print(arr2)

# ls= arr1.tolist()
# print(ls)
# ls1= [1,2,3]

print()

# for n,item in enumerate(arr1.tolist()):
#     print(f"{n} => {item}")


arr_byte= array('b',[18,102,56,60,100,56,-56,-20])
print(arr_byte.typecode)
# arr_byte.append(256)    
arr_byte.append(-2)    
print(arr_byte)

# pop() :- This function removes the element at the position mentioned in its argument, and returns it.

# remove() :- This function is used to remove the first occurrence of the value mentioned in its arguments.

# index() :- This function returns the index of the first occurrence of value mentioned in arguments.

# reverse() :- This function reverses the array.

arr_byte.pop(1)
print(arr_byte)

arr_byte.remove(56)
print(arr_byte)

print("-20 position: ",arr_byte.index(-20))

arr_byte.reverse()
print(arr_byte)



