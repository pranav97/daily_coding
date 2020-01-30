"""
This problem was asked by Uber.

Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].
"""


def product_except_i(array):
    ret = []
    prod = 1
    for i in array:
        prod = prod * i
    for i in range(len(array)):
        # print(prod/array[i])
        ret.append(prod / array[i])
    return ret

assert(product_except_i([1, 2, 3, 4, 5])    == [120, 60, 40, 30, 24])
assert(product_except_i([3, 2, 1])          == [2, 3, 6])
