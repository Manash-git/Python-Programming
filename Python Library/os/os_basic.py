import os,sys


# cmnd= 'mkdir fuck_lol'
# fl= os.popen(cmnd,'r',1)
# print(fl)
fn= "new.txt"
fl= os.popen(fn,'w',1)
# fl.write("Hello World")
os.write(fl,'Hello World')
fl.close()

# os.rename(fd,"new.txt")



# os.mkdir("newdir")
# os.rename("newdir","dir")
# os.rmdir("dir")






# print(os.name)
# print(os.getcwd())

# print(os.path)
# print(os.path.abspath(""))

# print(os.listdir())