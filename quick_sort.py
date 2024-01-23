'''
A python implementation of quicksort
pseudo code from Grokking Algorithms Chapter 4
'''


def quick_sort(array: list) -> list:
    '''
    pick the first item as pivot
    (How to sort them in place in python?)
    '''
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = []
        greater = []
        for i in range(1, len(array)):
            if array[i] <= pivot:
                less.append(array[i])
            else:
                greater.append(array[i])

        left = quick_sort(less)
        left.append(pivot)
        right = quick_sort(greater)
        left.extend(right)
        return left


def main():
    array = [807, 1, 23, -49, 68, 3256]
    sorted_array = quick_sort(array)
    print(f"Sorted array is: {sorted_array}")


if __name__ == "__main__":
    main()
