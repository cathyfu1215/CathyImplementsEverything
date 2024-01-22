/* A C implementation of insertion sort */

# include <stdio.h>

void swap(int *p1, int *p2){
    int temp = *p1;
    *p1 = *p2;
    *p2 = temp;
}

void insertion_sort(int array[], int size){
    for(int i = 0; i < size; i++){
        for(int j = i + 1; j > 0; j--){
            if(array[j] < array[j-1]){
                swap(array + j, array + j - 1);
            }
        }
    }
}

int main(){
    int array[] = {13, 5, 1, 7, 2, 8, 21};
    int size = 7;
    insertion_sort(array, size);
    printf("The sorted list is :\n");
    for(int i = 0; i < size; i++){
        printf("%d\t", array[i]);
    }
    printf("\n");

    int array2[] = {33,888, 13, 5, 1, 7, 2, -8, 21};
    int size2 = 9;
    insertion_sort(array2, size2);
    printf("The sorted list is :\n");
    for(int i = 0; i < size2; i++){
        printf("%d\t", array2[i]);
    }
    printf("\n");
}