"""
Write a function that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does
not occur in A.

For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.

Given A = [1, 2, 3], the function should return 4.

Given A = [−1, −3], the function should return 1.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
each element of array A is an integer within the range [−1,000,000..1,000,000].
"""


def compute_smallest_positive(a: list) -> int:
    sorted_a = sorted(set(a))
    answer = 1
    for index, number in enumerate(sorted_a):
        if number > 0:
            current = sorted_a[index]
            if index < len(sorted_a) - 1:
                next = sorted_a[index + 1]
                if current + 1 == next:
                    continue
                else:
                    answer = current + 1
                    break
            else:
                answer = current + 1
    return answer


if __name__ == '__main__':
    A = [1, 3, 6, 4, 1, 2]
    result = compute_smallest_positive(A)
    print(f'{result} is the smallest positive number')
