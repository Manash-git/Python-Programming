"""
pattern Demo
        ******
        *****
        ****
        ***
        **
        *
        
"""

def triangle_pettern(n):
    for i in range(n,-1,-1):
        for j in range(0,i+1):
            print("*  ",end="")
        print("")
print("Desire Output:\n")
triangle_pettern(10)
         
