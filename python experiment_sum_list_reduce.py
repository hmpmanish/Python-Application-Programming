""" Calculate the sum of the list using reduce """

from functools import reduce

n = [2, 4, 6, 812, 55]
total = reduce(lambda x, y: x + y, n)

print("Sum of the list:", total)
