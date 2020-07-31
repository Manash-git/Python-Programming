def div_3_and_5(n):
    
    res=[]
    
    for i in range(n):
        if i%3==0 and i%5 == 0:
            res.append(i)
    return res

print(div_3_and_5(50))

nums = [13, 11, 16, 78, 31, 128,23]
print("Sum of list => ",sum(nums))
print("Largest elements of a list=> ",max(nums))