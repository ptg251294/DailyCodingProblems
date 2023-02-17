# Given an array of N non-negative integers arr[] representing an elevation map where the width of each bar is 1,
# compute how much water it is able to trap after raining.

def pool_volume(wall_array, array_length):
    volume = 0
    left_max = 0  # highest wall to the left
    right_max = 0  # highest wall to the right

    start = 0  # start index of list
    end = array_length - 1  # end index of list

    while start <= end:
        if wall_array[start] < wall_array[end]:
            if wall_array[start] > left_max:
                left_max = wall_array[start]
            else:
                volume += left_max - wall_array[start]
            start += 1
        else:
            if wall_array[end] > right_max:
                right_max = wall_array[end]
            else:
                volume += right_max - wall_array[end]
            end -= 1

    return volume


if __name__ == '__main__':
    arr = [5, 4, 0, 2, 6, 0, 1]
    n = len(arr)
    print("Maximum water that can be accumulated is ", pool_volume(arr, n))
