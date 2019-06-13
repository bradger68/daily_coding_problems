"""Given an array of integers, write a function to determine
whether the array could become non-decreasing by modifying at
most 1 element.

For example, given the array [10, 5, 7], you should return true,
since we can modify the 10 into a 1 to make the array non-decreasing.

Given the array [10, 5, 1], you should return false, since we can't
modify any one element to get a non-decreasing array. """


# So I'm thinking I should create a function that checks if
# the list is increasing, and if it finds an element
# that is not increasing, it will add that to a count,
# and if the count is greater than 1, it returns false!


def is_increasing(my_list):
    count = 0
    current_spot = 0
    for num in range(len(my_list)-1):
        if my_list[num] > my_list[num+1]:
            count += 1
    if count > 1:
        return False
    else:
        return True


exampleTrue = [10, 5, 7]
exampleFalse = [10, 5, 1]

print(is_increasing(exampleTrue))
print(is_increasing(exampleFalse))
