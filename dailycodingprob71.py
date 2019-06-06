""" Using a function rand7() that returns an integer from 1 to 7 (inclusive)
with uniform probability, implement a function rand5() that returns an integer
from 1 to 5 (inclusive)."""


import random

def rand7():
    return random.randint(1,7)

# print(rand7())


def rand5():
    my_number = rand7()
    while my_number > 5:
        my_number = rand7()
    return my_number

print(rand5())
