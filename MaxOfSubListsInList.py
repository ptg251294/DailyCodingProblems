# This problem was asked by Google.
#
# Given an array of integers and a number k, where 1 <= k <= length of the array, compute the maximum values of each
# sub array of length k.
#
# For example, given array = [10, 5, 2, 7, 8, 7] and k = 3, we should get: [10, 7, 8, 8], since:
#
# 10 = max(10, 5, 2)
#
# 7 = max(5, 2, 7)
#
# 8 = max(2, 7, 8)
#
# 8 = max(7, 8, 7)
#
# Do this in O(n) time and O(k) space. You can modify the input array in-place and you do not need to store the
# results. You can simply print them out as you compute them.

def max_values_of_sub_array(int_arr, k):
    for index in range(0, len(int_arr) - k + 2):
        print(max(int_arr[index: index + k]))


if __name__ == '__main__':
    input_arr = input().split(',')
    int_arr = []
    for i in range(len(input_arr) - 1):
        int_arr.append(int(input_arr[i]))
    k = int(input())
    max_values_of_sub_array(int_arr, k)
