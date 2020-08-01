def reverse_num(n):
    result = 0
    
    while n>0:
        last_digit = n%10
        result = result*10 + last_digit
        n= n//10
    return result

print(reverse_num(153))