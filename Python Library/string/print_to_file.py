sourceFile= open("Data.txt",'w')

x,y= 10,15

print(f"It is amazing to see.\n{x} * {y} => {x*y}",file=sourceFile)

print("test Done. ok",file=sourceFile)

sourceFile.close()