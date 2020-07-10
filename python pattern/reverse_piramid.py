def pettern(n):
    for line in range(1,n+1):
        for space in range(1,line):
            print(" ",end="")
        for star in range(line, n+1):
            print("* ",end="")
        print("")

pettern(10)

print()
def rev_pir_adv(n):
    for line in range(n):
        print(" "*line + "* "*(n-line))
rev_pir_adv(5)

# odd reverse
print()
def odd_rev_pir_adv(n):
    for line in range(n):
        print("  "*line + "* "*(n-(2*line)))
odd_rev_pir_adv(5)

# even reverse
print()
def even_rev_pir_adv(n):
    for line in range(n):
        print("  "*line + "* "*(n-(2*(line+1))))
even_rev_pir_adv(7)

         
         
     