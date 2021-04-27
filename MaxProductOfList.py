# This problem was asked by Facebook.
#
# Given a list of integers, return the largest product that can be made by multiplying any three integers.
#
# For example, if the list is [-10, -10, 5, 2], we should return 500, since that's -10 * -10 * 5.
#
# You can assume the list has at least three integers.

def product_of_negative():
    if sorted_list[1] < 0:
        test = (sorted_list[0] * sorted_list[1])
        return test


def call_if_pair_of_negative():
    x = a * sorted_list[input_list_length - 1]
    y = b * sorted_list[input_list_length - 3]
    if y < x:
        print(x)
    else:
        print(y)


def product_of_positives():
    return sorted_list[input_list_length - 1] * sorted_list[input_list_length - 2]


def call_if_single_negative():
    print(sorted_list[input_list_length - 1] * sorted_list[input_list_length - 2] * sorted_list[input_list_length - 3])


global a, b

if __name__ == '__main__':
    input_list = [-19, -15, 3, 25, 9, 12]
    sorted_list = sorted(input_list)
    input_list_length = (len(sorted_list))
    a = product_of_negative()
    b = product_of_positives()
    if sorted_list[1] < 0:
        call_if_pair_of_negative()
    else:
        call_if_single_negative()
