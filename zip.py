from zipfile import *
f=ZipFile("D:\\pp1.zip",'w',ZIP_DEFLATED)
print(type(f))
f.write("file1.txt")
f.write("file3.txt")
f.write("file2.txt")
f.close
print("zip created")

