# This question was asked by JPMorgan Chase. Given a string containing digits from 2-9 inclusive,
# return all possible letter combinations that the number could represent. Return the answer in any order.
#
# A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any
# letters.


from typing import List


def letter_combinations(digits: str) -> List[str]:
    combinations = []
    if digits.__len__() == 0:
        return []
    digit = keys_dictionary[digits[0]]
    str1 = list(digit)
    str2 = digits[1:digits.__len__()]
    if digits.__len__() == 1:
        return list(digit)
    else:
        for c1 in str1:
            for c2 in letter_combinations(str2):
                combinations.append(c1 + c2)
    return combinations


if __name__ == '__main__':
    keys_dictionary = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
    }
    print(letter_combinations('234'))
