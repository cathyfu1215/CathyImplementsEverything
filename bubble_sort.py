'''
A python implementation of bubble sort
'''


def swap(array: list, index1: int, index2: int) -> None:
    temp = array[index1]
    array[index1] = array[index2]
    array[index2] = temp


def bubble_sort(array: list) -> None:
    for i in range(len(array)-1, -1, -1):
        for j in range(0, i):
            if array[j] > array[j+1]:
                swap(array, j, j+1)
        # verify
        print(f"After the {len(array)-i}th iteration, the array is: ")
        print(array)


def main():
    list1 = [103, 22, 367, 5, -8, 13]
    bubble_sort(list1)
    print("The sorted array is: ")
    print(list1)


if __name__ == "__main__":
    main()
