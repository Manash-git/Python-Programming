import string

str1= 'The quick brown Fox jump over the lazy Dogs on 1st of December'

# res="".join(i for i in str1 if i in string.ascii_letters)
# print(res)

# print(" - ".join(x for x in str1 if x in string.ascii_uppercase))
# print()
# print(" ~ ".join(x for x in str1 if x in string.ascii_lowercase))

str2='DarkKnight'

# # space is not a alphanumeric 

# print(str1.isalnum())
# print(str2.isalnum())

# print(str1.isalpha())
# print(str2.isalpha())

dec= "12345"
dec1= "1234B"
print(dec.isnumeric())
print(dec1.isnumeric())

# Syntax:  all(iterable)
# True - If all elements in an iterable are true
# False - If any element in an iterable is false

print(all(i.isalpha() for i in str1))
print(all(i.isalpha() for i in str2))


