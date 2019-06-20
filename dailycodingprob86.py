"""Given a string of parentheses, write a function
to compute the minimum number of parentheses to be
removed to make the string valid (i.e. each open parenthesis
is eventually closed).

For example, given the string "()())()", you should return 1.
Given the string ")(", you should return 2, since we must remove all of them. """

input1 = "()()()())))"
input2 = ")("


def find_parentheses(input):
    count = 0
    for character in range(len(input)):
        if input[character] == "(":
            if input[character+1] != ")":
                count += 1
        elif input[character] == ")":
            if input[character-1] != "(":
                count += 1
    return count


print(find_parentheses(input1))
# print(find_parentheses(input2))

# This is returning an error for input2 because it's out of
# range. Still figuring out a solution to that. 
