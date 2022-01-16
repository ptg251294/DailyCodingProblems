"""
This problem was asked by Google.
Given an array of numbers and an index i, return the index of the nearest larger number of the number at index i, where
distance is measured in array indices.
For example, given [4, 1, 3, 5, 6] and index 0, you should return 3.
If two distances to larger numbers are the equal, then return any one of them. If the array at i doesn't have a
nearest larger integer, then return null.
Follow-up: If you can preprocess the array, can you do this in constant time?
"""


def nearest_max(numbers, ind):
    lis = []
    for i in range(len(numbers)):
        if numbers[i] > numbers[ind]:
            lis.append(numbers[i])
            if lis is None:
                return
            else:
                return numbers.index(min(lis))


if __name__ == '__main__':
    a = [4, 1, 3, 5, 10, 2]
    index = 0
    answer = nearest_max(a, index)
    print(answer)
    
