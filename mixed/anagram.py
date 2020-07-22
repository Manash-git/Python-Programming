str1= "manashe"
str2= "samnah"

# Two strings will be anagram if they contains same character bt in different order

if sorted(str1)==sorted(str2):
    print("Both are Anagram")
else:
    print("Not Anagram")