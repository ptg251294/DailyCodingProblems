# This problem was asked by Bloomberg.
#
# Determine whether there exists a one-to-one character mapping from one string s1 to another s2.
#
# For example, given s1 = abc and s2 = bcd, return true since we can map a to b, b to c, and c to d.
#
# Given s1 = foo and s2 = bar, return false since the o cannot map to two characters.

def mapping():
    dictionary = {}
    for i in range(len(str1)):
        if str1[i] in dictionary and str2[i] != dictionary.get(str1[i]):
            return False
        else:
            dictionary[str1[i]] = str2[i]
    print('mapping------------>', dictionary)
    return True


if __name__ == '__main__':
    str1 = 'abc'
    str2 = 'bcd'
    print(mapping() if len(str1) == len(str2) and len(str1) > 0 and len(str2) > 0 else False)
