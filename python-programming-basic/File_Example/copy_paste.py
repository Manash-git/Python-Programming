fr= open("data.txt","r")
fw=open("demofile1.txt",'w')

for i in fr:
    fw.write(i)
