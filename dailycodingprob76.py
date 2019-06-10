""" You are given an N by M 2D matrix of lowercase letters. Determine
the minimum number of columns that can be removed to ensure that each
row is ordered from top to bottom lexicographically. That is, the letter
at each column is lexicographically later as you go down each row. It
does not matter whether each row itself is ordered lexicographically.

For example, given the following table:

cba
daf
ghi

This is not ordered because of the a in the center. We can remove the
second column to make it ordered:

ca
df
gi

So your function should return 1, since we only needed to remove 1 column.

As another example, given the following table:

abcdef

Your function should return 0, since the rows are already ordered (there's
only one row).

As another example, given the following table:

zyx
wvu
tsr

Your function should return 3, since we would need to remove all the
columns to order it."""

# First I am going to make a function that finds the "largest" letter
# in a given column.

def find_largest_letter(my_column):
        return max(my_column)


# Alrighty, now to check each column and delete it if it has a letter
# "smaller" than the "largest" letter in the previous column.
# Be sure to keep a count of how many columns were deleted.

# Just kidding, my find_largest_letter function isn't actually necessary.


def check_columns(my_matrix):
    num_of_columns = len(my_matrix[0])
    rows = len(my_matrix)
    count = 0
    for col in range(num_of_columns):
        for row in range(1, rows):
            if my_matrix[row][col] < my_matrix[row-1][col]:
                count += 1
                break
    return count


my_matrix = ['zyx', 'wvu', 'tsr']

print(check_columns(my_matrix))
