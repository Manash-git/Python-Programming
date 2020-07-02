
from encodings.aliases import aliases
# print(aliases)


count = 1

for i in aliases:
    # print(count,i)
    count+=1
    
import codecs

print(codecs.encode("I love You","rot13"))

encrypted = codecs.encode("I love You","rot13")
print(encrypted)

print(codecs.decode(encrypted,"rot13"))

# Decode + Encode in a single line
print(codecs.decode(codecs.encode("I love You","rot13"),"rot13"))
