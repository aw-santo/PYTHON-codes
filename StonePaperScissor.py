import random

a = random.randint(0, 2)
st = input("YourTurn : ")
st = st.lower()
st1 = ""
if a == 0:
    st1 = "stone"
elif a == 1:
    st1 = "paper"
elif a == 2:
    st1 = "scissor"

print("Computer's turn : ",st1)

if st == "stone":
    if a == 0:
        print("Round drawn!☺")
    elif a == 1:
        print("You lose!")
    elif a == 2:
        print("You won!☻")

if st == "paper":
    if a == 0:
        print("You won!☻")
    elif a == 1:
        print("Round drawn!☺")
    elif a == 2:
        print("You lose!")

if st == "scissor":
    if a == 0:
        print("You lose!")
    elif a == 1:
        print("You won!☻")
    elif a == 2:
        print("Round drawn!☺")
