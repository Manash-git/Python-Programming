age = 25
# Conditions are evaluated from left to right
# print('kid' if age < 18 else 'adult')

# print("kid" if age<20 else "Teen")

print(age>21)

# format:  (False, True)[True]
print(("child","Young")[age>21])



print("\n\n")
if age < 18:
    if age < 12:
        print('kid')
    else:
        print('teenager')
else:
    print('adult')

# Above code eqauvalent

# print('kid' if age < 13 else 'teenager' if age < 18 else 'adult')