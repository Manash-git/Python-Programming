import os,tempfile

# f= tempfile.mkstemp(suffix='.man')

# f= tempfile.TemporaryDirectory(dir="C:\Users\crazy\AppData\Local\Temp\mytemp")
# print(tempfile.gettempdir())
(f_temph,f_tempf)= tempfile.mkstemp(suffix=".tp")
# f_temp= tempfile.mkstemp(suffix=".tp")
# print(f_temph.name)
print(f_temph,f_tempf)

f= os.fdopen(f_temph,'w+')

f.write("Hello world")
f.seek(0)
print(f.read())
f.close()
os.remove(f_tempf)