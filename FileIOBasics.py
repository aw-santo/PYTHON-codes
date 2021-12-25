# File IO basics

"""
"r" - open file for reading - default
"S" - open file for writing
"x" - creates file if not exists
"a" - append in file
"t" - text mode - default
"b" - binary mode
"+" - both read and write

 """

f = open("FileIOBasics.txt", "rt")
# for l in f:
#     print(l, end="")
# print(f.readline())
# print(f.readline())
# print(f.readline())
# print(f.readlines())

con = f.read()
print(con)
# con = f.read(5)
# print(con)
# c = f.read(7865)
# print(c)
f.close()
