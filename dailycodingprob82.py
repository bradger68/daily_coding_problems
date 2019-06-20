"""Using a read7() method that returns 7 characters
from a file, implement readN(n) which reads n characters.

For example, given a file with the content "Hello world",
three read7() returns "Hello w", "orld" and then "". """


def read7(my_entry):
    current_place = 0
    while current_place in range(len(my_entry)):
        print(my_entry[current_place: current_place+7])
        current_place += 7


def readN(my_entry, N):
    current_place = 0
    while current_place in range(len(my_entry)):
        print(my_entry[current_place: current_place + N])
        current_place += N




# read7("Hello World")
readN("Hello World", 7)
readN("Hello World", 10)
