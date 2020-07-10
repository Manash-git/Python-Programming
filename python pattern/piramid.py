def pir(n):
    for line in range(1,n+1):
        for space in range(0,n-line):
            print(end=" ")
        for star in range(line):
            print("* ",end="")
        print()
pir(10)

# shortcut code for piramid
print()
def pir_advance(n):
    for line in range(1,n+1):
        print(" "* (n-line) + "* " * line)
pir_advance(10)

# odd piramid
print()
def pir_odd(n):
    for line in range(n):
        print("  "*(n-line-1)+"* "*((2*line)+1))
pir_odd(5)

# even piramid
print()
def pir_even(n):
    for line in range(n):
        print("  "*(n-line-1)+"* "*((2*line)))
pir_even(6)