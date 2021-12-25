a = int(input("Enter your age : "))
if a > 14:
    if a < 80:
        if a > 18:
            print("You can drive☻")

        elif a == 18:
            print("Cant decide, come to the center!")

        else:
            print("You cant drive!")

elif a <= 14:
    print("You are too small for training also!")

elif a >= 80:
    if a < 102:
        print("You shouldn't drive!")

else:
    print("Invalid age!")
