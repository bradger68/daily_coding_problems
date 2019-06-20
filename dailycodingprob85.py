"""Given three 32-bit integers x, y, and b, return x
if b is 1 and y if b is 0, using only mathematical or
bit operations. You can assume b can only be 1 or 0. """

def x_or_y(x, y, b):
    if b == 0:
        return x
    elif b == 1:
        return y
    else:
        print("b must be 0 or 1.")

print(x_or_y(5, 10, 0))
print(x_or_y(5, 10, 1))
print(x_or_y(5, 10, 5))
