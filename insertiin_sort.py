'''
A python implementation of insertion sort
'''


def swap(array: list, i: int, j: int) -> None:
    temp = array[i]
    array[i] = array[j]
    array[j] = temp


def insertion_sort(array: list) -> list:
    '''
    logic: Set bar at index 0 and it moves onwards.
           Set current at bar + 1 and it moves backwards.
           Compare each "current" item with the item before it.
           If the left neighbout is smaller,
           this is the right position of the current item.
           Otherwise, swap the item with its left neighbour
           keep comparing until the current item reaches the
           right place it should go
    '''
    for bar in range(0, len(array) - 1):
        for current in range(bar+1, 0, -1):
            # print(f"current array is :{array}")
            if array[current] < array[current - 1]:
                swap(array, current, current - 1)

    return array


def main():
    array = [13, 5, 1, 7, 2, 8, 21]
    insertion_sort(array)
    print("Sorted array is: ", array)


if __name__ == "__main__":
    main()
