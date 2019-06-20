"""Given a mapping of digits to letters (as in a phone number),
and a digit string, return all possible letters the number could
represent. You can assume each valid number in the mapping is a single digit.

For example if {"2": ["a", "b", "c"], 3: ["d", "e", "f"], …} then "23"
should return ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]. """

digits_to_letters = {
    "2": ["a", "b", "c"],
    "3": ["d", "e", "f"],
    "4": ["g", "h", "i"],
    "5": ["j", "k", "l"],
    "6": ["m", "n", "o"],
    "7": ["p", "q", "r", "s"],
    "8": ["t", "u", "v"],
    "9": ["w", "x", "y", "z"]
}


valid_entries = ["2", "3", "4", "5", "6", "7", "8", "9"]

def entry_to_list(entry):
    my_list = []
    for character in entry:
        if character in valid_entries:
            my_list.append(character)
        else:
            pass
    return my_list


def find_letter_strings(my_entry):

    if not my_entry:
        return

    if len(my_entry) == 1:
        return digits_to_letters[my_entry[0]]

    my_list = list()
    current_letters = digits_to_letters[my_entry[0]]
    strings_of_rem_nums = find_letter_strings(my_entry[1:])
    for letter in current_letters:
        for string in strings_of_rem_nums:
            my_list.append(letter + string)

    return my_list



print(find_letter_strings("23"))
print(find_letter_strings("32"))
# print(find_letter_strings("1"))
