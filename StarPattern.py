a = int(input("Enter the no. of rows : "))
# b = bool(input("For normal patter : 1  |   For inverted pattern : 0 "))
c = 0
d = 0
while c < a:
    # if b:
    while d < c+1:
        print('*', end="")
        d += 1
    print()
    c += 1
