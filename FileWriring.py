# To open a file in write or append form

# f = open("FileIOBasics2.txt", "w")
# # f = open("FileIOBasics2.txt", "a")
# a = f.write("You're right!\n")
# print(a)
# f.close()


# To open file in read and write form

f = open("FileIOBasics2.txt", "r+")
print(f.read())
f.write("tnx")