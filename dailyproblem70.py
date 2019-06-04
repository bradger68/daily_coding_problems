"""A number is considered perfect if its digits sum up to exactly 10.

Given a positive integer n, return the n-th perfect number.

For example, given 1, you should return 19. Given 2, you should return 28."""

def is_perfect(number):
  number = str(number)
  digits = []
  for digit in number:
    digits.append(int(digit))
  sum_of_digits = sum(digits)
  if sum_of_digits == 10:
    return True


print(is_perfect(19))
print(is_perfect(28))
print(is_perfect(52))
