import zipfile

# print(dir(zipfile))

# print(dir(zipfile.ZipFile))

# try:
#     with zipfile.ZipFile("file.zip") as fl:
#         print("ok")
# except zipfile.BadZipFile:
#     print("Error: File corrupted.")

# zipFile.getinfo("file.zip")
# print(getinfo("file.zip"))

# ZipFile.read(name="file.zip",pwd=None)

print(zipfile.is_zipfile("file.zip"))


# with zipfile.ZipFile("file.zip") as zp:
#     print(zp.infolist())
#     print(zp.namelist())
#     # zp.extractall()
#     zp.extract("demo.txt")
#     zp.extract("test.txt")
    
#     # zipfile.getinfo(zp)