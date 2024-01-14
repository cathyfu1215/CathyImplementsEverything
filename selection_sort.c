/*
A C implementation of selection sort
from Grokking Algo textbook Ch2

Learned from https://www.geeksforgeeks.org/selection-sort/

Thoughts: 
0. I need to read about pointers and arrays of C carefully, 
   and practice more!
1. I need to learn and practice more sorting algorithms.

15 Sorting Algorithms in 6 Minutes
https://www.youtube.com/watch?v=kPRA0W1kECg
*/


# include <stdio.h>

void swap(int *pa, int *pb){
    int temp = *pa;
    *pa = *pb;
    *pb = temp;
}

void selection_sort(int array[], int size){
    
    int i; // the index of the current smallest item
    int j;
    int smallest_value;

    for (i = 0; i < size;i++){ 
        // each step in this loop tackle one smallest item
        
        smallest_value = array[i];
        for(j = i + 1; j < size; j++){
            if(smallest_value > array[j]){
                smallest_value = array[j];
                swap(&array[i], &array[j]);
            }
        }

    }
}

int main(void){
    int array[] = {1, 31, 4, 5, 78, 69};
    int size = 6;
    printf("The initial array is: \n");
    for(int i = 0;i < size; i++){
        printf("%d\t", array[i]);
    }
    printf("\n");
    selection_sort(array, size);
    printf("The sorted array is :\n");
    for(int i = 0;i < size; i++){
        printf("%d\t", array[i]);
    }
    return 0;
}
