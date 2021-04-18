# Compute the running median of a sequence of numbers. That is, given a stream of numbers, print out the median of
# the list so far on each new element.
#
# Recall that the median of an even-numbered list is the average of the two middle numbers.
#
# For example, given the sequence [2, 1, 5, 7, 2, 0, 5], your algorithm should print out:
#
# 2
# 1.5
# 2
# 3.5
# 2
# 2
# 2

def print_median(input_list):
    if len(input_list) == 1:
        median = input_list[0]
        print(median)
    elif (len(input_list) % 2) == 0:
        input_list.sort()
        first = int((len(input_list) / 2) - 1)
        second = int(len(input_list) / 2)
        median = (input_list[first] + input_list[second]) / 2
        print(median)
    else:
        input_list.sort()
        pos = int(len(input_list) / 2)
        median = input_list[pos]
        print(median)


if __name__ == '__main__':
    source_list = [2, 1, 5, 7, 2, 0, 5]
    input_list = []
    for index in range(len(source_list)):
        input_list.append(source_list[index])
        print_median(input_list)