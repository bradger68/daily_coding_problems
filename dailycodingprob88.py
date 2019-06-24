"""Implement division of two positive integers without
using the division, multiplication, or modulus operators.
Return the quotient as an integer, ignoring the remainder. """

def divide(number, divided_by):
    count = 0
    total = 0
    while total < number:
        count += 1
        total += divided_by
    return count

print(divide(10,5))
print(divide(9,3))
print(divide(9,4))
print(divide(1,1))
