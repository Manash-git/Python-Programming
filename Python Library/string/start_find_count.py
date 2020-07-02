text= 'The quick brown Fox jump over the lazy Dogs and Fox'

# Start and End with specific string

# print(text.startswith("The"))
# print(text.startswith("the"))

# print(text.startswith('Fox'))

# print(text.endswith("dogs"))
# print(text.endswith("Dogs"))

# # find a string

# print(text.find("The"))
print(text.find("Fox"))
print(text.rfind("Fox"))
# print(text.rfind("Dogs"))
# print(text.find("dogs"))

quote = 'Do small things with great love'

# Substring is searched in 'hings with great love'
# print(quote.find('small things', 10))

# Substring is searched in ' small things with great love' 
# print(quote.find('small things', 2))

# Substring is searched in 'hings with great lov'
# print(quote.find('o small ', 10, -1))

# Substring is searched in 'll things with'
print(quote.find('things ', 6, 20))

quote = 'Let it be, let it be, let it be'

result = quote.rfind('let it')
print("Substring 'let it':", result)

print(quote.find('let it'))

print(text.count("bat"))
print(text.count("fox"))
print(text.count("Fox"))
print(text.count("brown"))