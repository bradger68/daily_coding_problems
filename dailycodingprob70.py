"""A number is considered perfect if its digits sum up to exactly 10.

Given a positive integer n, return the n-th perfect number.

For example, given 1, you should return 19. Given 2, you should return 28."""

def find_nth_perfnum(n):
  temporary_sum = 0
  for digit in str(n):
    temporary_sum += int(digit)

  return (n * 10) + (10- temporary_sum)


print(find_nth_perfnum(1))
print(find_nth_perfnum(2))
print(find_nth_perfnum(19))




# The following function just verifies whether or not
# an integer is perfect or not. It does not find 
# the nth perfect number. I originally started 
# coding it out like this but realized there was 
# an easier way to do it after looking at solution 
# from github user Vineetjohn


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
