# a = 3
# b = 4
# c = pow(a,b,)
# print(c)
from builtins import bool


def func():
    print("you are in func!")


func()


def func2(a, b):
    """This func return the average of two numbers!"""          #Docstring
    average = (a + b) / 2
    print(average)
    return average


# v = func2(4, 8)
# print(v)
print(func2.__doc__)
