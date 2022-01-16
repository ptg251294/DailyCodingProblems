"""
This problem was asked by Uber.
One way to unlock an Android phone is through a pattern of swipes across a 1-9 keypad.
For a pattern to be valid, it must satisfy the following:
All of its keys must be distinct.
It must not connect two keys by jumping over a third key, unless that key has already been used.
For example, 4 - 2 - 1 - 7 is a valid pattern, whereas 2 - 1 - 7 is not.
Find the total number of valid unlock patterns of length N, where 1 <= N <= 9.
"""

not_possible_source = {
    1: [3, 7, 9],
    2: [8],
    3: [1, 7, 9],
    4: [6],
    5: [],
    6: [4],
    7: [1, 3, 9],
    8: [2],
    9: [7, 1, 3]
}


def check_input_pattern(start, inp_str):
    for i in range(1, len(inp_str)):
        if not_possible_source[int(start)].__contains__(int(inp_str[i])):
            return False
        else:
            start = inp_str[i]
    return True


if __name__ == '__main__':
    inp = '1-2-3-4'
    inp_str = inp.replace('-', '')
    start = inp_str[0]
    valid_pattern = check_input_pattern(start, inp_str)
    print('Valid pattern') if valid_pattern else print('Invalid pattern')
