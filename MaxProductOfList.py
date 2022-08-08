# This problem was asked by Facebook.
#
# Given a list of integers, return the largest product that can be made by multiplying any three integers.
#
# For example, if the list is [-10, -10, 5, 2], we should return 500, since that's -10 * -10 * 5.
#
# You can assume the list has at least three integers.

def negative_pair_product():
    return (sorted_list[0] * sorted_list[1]) if sorted_list[1] < 0 else None


def call_if_pair_of_negative(least_negative_pair_product, max_positive_pair_product):
    x = least_negative_pair_product * sorted_list[input_list_length - 1]
    y = max_positive_pair_product * sorted_list[input_list_length - 3]
    print(x) if y < x else print(y)


def positives_pair_product():
    return sorted_list[input_list_length - 1] * sorted_list[input_list_length - 2]


def call_if_single_negative():
    print(sorted_list[input_list_length - 1] * sorted_list[input_list_length - 2] * sorted_list[input_list_length - 3])


if __name__ == '__main__':
    input_list = [-19, -15, 3, 25, 9, 12]
    sorted_list = sorted(input_list)
    input_list_length = (len(sorted_list))
    a = negative_pair_product()
    b = positives_pair_product()
    if sorted_list[1] < 0:
        call_if_pair_of_negative(a, b)
    else:
        call_if_single_negative()
