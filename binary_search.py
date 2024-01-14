'''
A python implementation of binary search slightly different
from Grokking Algo textbook
'''

import math


def binary_search(list: list, item: int) -> int or None:
    '''
    >>> list1 = [1, 2, 3, 5, 8, 13]
    >>> binary_search(list1, 3)
    2
    >>> list1 = [1, 2, 3, 5, 8, 13]
    >>> binary_search(list1, 18) is None
    True
    >>> list1 = [1, 2, 3, 5, 8, 13]
    >>> binary_search(list1, -1) is None
    True
    >>> list1 = [1, 2, 3, 5, 8, 13]
    >>> binary_search(list1, 1)
    0
    >>> list1 = [1, 2, 3, 5, 8, 13]
    >>> binary_search(list1, 13)
    5
    '''

    low = 0
    high = len(list) - 1

    while low <= high:

        # mid should be in the while loop so after high or low gets updated,
        # mid gets updated, too
        mid = math.floor((high + low)/2)

        guess = list[mid]

        if guess == item:
            return mid
        else:
            if guess < item:
                low = mid + 1
            else:
                high = mid - 1
    return None


def main():
    list1 = [1, 2, 3, 5, 8, 13]
    answer = binary_search(list1, 5)  # should be 3
    print(answer)
    list2 = [1, 2, 3, 5, 8, 13]
    answer = binary_search(list2, -5)  # should be None
    print(answer)


if __name__ == "__main__":
    main()
