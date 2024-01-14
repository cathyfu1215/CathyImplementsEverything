'''
Implementing seletion sort in python
using the pseudo code in Grokking Algorithms
'''


def find_smallest(array: list) -> int:
    '''
    consumes an array of values,
    return the index of the smallest one

    >>> find_smallest([1,2,3,4])
    0
    >>> find_smallest([2,1,3,4])
    1
    >>> find_smallest([10,2,3,4,1])
    4
    >>> find_smallest([])
    Traceback (most recent call last):
    ...
    ValueError: array should be non-empty

    '''
    if len(array) == 0:
        raise ValueError("array should be non-empty")

    smallest = array[0]
    smallest_index = 0

    for i in range(0, len(array)):
        if smallest > array[i]:
            smallest = array[i]
            smallest_index = i
    return smallest_index


def selection_sort(array: list) -> list:
    '''
    consume a list of numbers, return the sorted list
    in ascending order

    >>> selection_sort([2,1,3,4])
    [1, 2, 3, 4]
    >>> selection_sort([5,2,1,3,4])
    [1, 2, 3, 4, 5]
    >>> selection_sort([])
    []
    '''
    sorted_array = []
    for i in range(0, len(array)):
        item = find_smallest(array)

        # The list pop() method removes the item at the specified index.
        # The method also returns the removed item.
        sorted_array.append(array.pop(item))
    return sorted_array


def main():
    try:
        array = [1, 31, 4, 5, 78, 69]
        print(selection_sort(array))
    except ValueError:
        print("Please enter an non-empty array!")


if __name__ == "__main__":
    main()
