# import string

text= "This is Python"

key=text.maketrans("asdfghjkl","12zxcvbnm")

print("Original String: ",text)
print("Encrypted String: ",text.translate(key))
print("Hello World".translate(key))



base= 'abcdef'
key= "xyzpqr"
ignore = "ae"

paragraph="abcdefghijkl"
trans_table=paragraph.maketrans(base,key)
print("encrypted: ",paragraph.translate(trans_table))

trans_table=paragraph.maketrans(base,key,ignore)
print("encrypted: ",paragraph.translate(trans_table))


# Here, the translation mapping translation contains the mapping from a, b and c to g, h and i respectively.
# But, the removal string thirdString resets the mapping to a and b to None.
# So, when the string is translated using translate(), a and b are removed, and c is replaced i outputting idef.


# Manual Translation table

table={97:98,
       98:99,
       99:100,
       100:101,
       101:102
       }


text1='abcde'
print(text1)
print("Manual encrypted: ",text1.translate(table))

# Another way of manual tranlation

tbl={97:'d',
     99:"T"
     }

test= "acxy"
print(test)
print("Test encrp: ",test.translate(tbl))