f = open('demofile.txt', 'w')

f.write('Woops! I have deleted the content!\n')

l= [10,20,30,50,60]

for i in l:
    f.write(str(i)+'\n')
    

f.close()


