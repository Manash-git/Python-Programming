# raw code
import string


def vowel(n):
    v=['a','e','i','o','u']
    if n in v:
        return True
    else:
        return False




s=['a','b','c','d','e']
res = filter(vowel,s)
# print(list(res))

print(list(filter(vowel,string.ascii_lowercase)))
# print(string.ascii_lowercase)
# print(string.ascii_uppercase)
# print(list(string.ascii_lowercase))

