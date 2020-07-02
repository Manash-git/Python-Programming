import os
import tempfile

# # print(tempfile.gettempdir())
# # print(tempfile.gettempprefix())
# # print(tempfile.gettempdirb())
# # print(tempfile.gettempprefixb())


# f= tempfile.TemporaryFile()
# f.write(b'\nWellcome \nWorld')
# print(f.name)
# # f.seek(os.SEEK_SET)
# f.seek(0)
# # print(f.read().decode('utf-8'))
# # f.seek(os.SEEK_SET)
# print(f.read())
# # f.seek(os.SEEK_SET)
# # f.seek(os.SEEK_END)
# # print(f.read())
# f.close()

# print('\n\n')

# f1= tempfile.TemporaryFile(mode='w+')
# print(f1)
# print(f1.name)
# f1.write("Hello world")
# f1.seek(0)
# print(f1.read())
# f1.seek(0)
# print(f1.read().encode("utf-8"))
# f.close()

# print("\n\n")

# # This is used add prefix and suffix to a temporary file
# temp1= tempfile.NamedTemporaryFile()
# print(temp1)
# print(temp1.name)
# temp1.close()

print("\n\nPrefix  + Suffix \n\n")

# tempfile.tempdir="/mytemp"
temp_file= tempfile.NamedTemporaryFile(prefix="Haha_",suffix="_LOL")

print(temp_file)
# print(temp_file.name)
print(tempfile.gettempdir())
temp_file.close()


