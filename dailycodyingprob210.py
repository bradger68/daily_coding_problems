"""A Collatz sequence in mathematics can be defined as follows. Starting with any positive integer:

if n is even, the next number in the sequence is n / 2
if n is odd, the next number in the sequence is 3n + 1
It is conjectured that every such sequence eventually reaches the number 1. Test this conjecture.

Bonus: What input n <= 1000000 gives the longest sequence?"""


# Make a function that will find the next n based on current n
# Check if the sequence goes to 1.

# This finds how many steps for the sequence to go to 1.
def findNextN(n):
    count = 1
    while n > 1:
        if n % 2 == 0:
            n = n/2
            count += 1
        elif n % 2 == 1:
            n = 3*n+1
            count += 1
    print(count)
    return True


print(findNextN(3))
print(findNextN(1000000))
