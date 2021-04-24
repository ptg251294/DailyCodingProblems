# This problem was asked by Google.
#
# Given a string of parentheses, write a function to compute the minimum number of parentheses to be removed to make
# the string valid (i.e. each open parenthesis is eventually closed).
#
# For example, given the string "()())()", you should return 1. Given the string ")(", you should return 2,
# since we must remove all of them.

def count_invalid_parentheses(input_string):
    count = 0
    invalid_count = input_string.find('(')
    for index in range(invalid_count, len(input_string)):
        if input_string[index] == '(':
            count += 1
        else:
            count -= 1
    return abs(count) + invalid_count


if __name__ == '__main__':
    given_string = '(((((()((('
    answer = count_invalid_parentheses(given_string)
    print(answer)
