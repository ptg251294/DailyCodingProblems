# This problem was asked by Stripe.
# Given an integer n, return the length of the longest consecutive run of 1s in its binary representation.
# For example, given 156, you should return 3.

k = 7306303
a = str(bin(k)).split('b')[1]
count = 0
length = 0
for i in range(len(a)):
    if a[i] == '1':
        count += 1
        if count > length:
            length = count
    if a[i] == '0':
        count = 0
print(length)
