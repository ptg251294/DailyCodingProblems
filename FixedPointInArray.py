# This problem was asked by Apple.
#
# A fixed point in an array is an element whose value is equal to its index. Given a sorted array of distinct
# elements, return list of fixed points, if they exists. Otherwise, return False.
#
# For example, given [-6, 0, 2, 3, 40], you should return [2, 3]. Given [1, 5, 7, 8], you should return False.

def matching_number(list_input):
    result_list = []
    for index in list_input:
        if index == list_input.index(index):
            result_list.append(index)
    print(sorted(result_list) if len(result_list) > 0 else False)


if __name__ == '__main__':
    input_list = [-6, 0, 2, 40, 4, 5, 7, 9]
    raw_list = []
    for i in range(0, len(input_list)):
        raw_list.append(input_list[i])
    matching_number(raw_list)
