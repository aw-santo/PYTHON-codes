from turtle import goto

print("** Hint : No. is in between 1 and 100 (including both)")
n = 77
g = 5


for i in range(5):
    g -= 1
    e = int(input("Enter the number : "))
    if e < n:
        print("Entered no. is lesser!")
    elif e > n:
        print("Entered no. is greater!")
    elif e == n:
        print("You won!☻")
        print("Gusses you take : ",i+1)
        break


    print("Guesses left : ",g)
print("Game Over!")


