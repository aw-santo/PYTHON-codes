a = int(input("Enter 1st num : "))
b = input("Enter the operation : ")
c = int(input("Enter 2nd num : "))

if b == "/":
    if a == 56 and c == 6:
        print("56/6 = 4")
    else:
        print(a, "/", c, "=", a / c)

elif b == "+":
    if a == 56 and c == 9:
        print("56+9 = 77")
    else:
        print(a, "+", c, "=", a + c)

elif b == '*':
    if a == 45 and c == 3:
        print("45*3 = 555")
    else:
        print(a, "*", c, "=", a * c)

else:
    print(a, "-", c, "=", a - c)
