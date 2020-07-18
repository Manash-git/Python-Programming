#  Pro way
name= "lolm"[::-1]
# print(name)

x= "manash"
# x= "mam"
print(x==x[::-1])
# print(x.find(x[::-1])==0)

# Traditioan way
def isPalindrome(x):
    '''
    if x<0:
        return False
    else:
        return str(x).find(str(x)[::-1])==0
        # print(type(str(x)))
    '''
    return False if x < 0 else x == int(str(x)[::-1])
    
# print(isPalindrome(101))
# print(isPalindrome(-121))
# print(isPalindrome(10))