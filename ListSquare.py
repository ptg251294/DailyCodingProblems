# This problem was asked by Google.
# Given a sorted list of integers, square the elements and give the output in sorted order.
# For example, given [-9, -2, 0, 2, 3], return [0, 4, 4, 9, 81].

def square(given_list):
    output_list = []
    for index in range(len(given_list)):
        output_list.append(given_list[index] * given_list[index])
        print(sorted(output_list))


if __name__ == '__main__':
    input_list = [-9, -2, 0, 2, 3]
    square(input_list)
