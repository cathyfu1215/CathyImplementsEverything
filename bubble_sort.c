/*
A C implementation of bubble sort
*/

# include <stdio.h>


void swap(int *pa, int *pb){
    int temp = *pa;
    *pa = *pb;
    *pb = temp;
};

void bubble_sort(int array[], unsigned int size){
    for (int i = size - 1; i>=1; i--){
        
        for(int j = 0; j <= i-1; j++){
            if(array[j] > array[j+1]){
                swap(array+j, array+j+1);
            }
        }
        //Verify: print every step and see the largest item bubbled to the bottom
        printf("\n");
        printf("After the %dth iteration, the array is:\n", size - i);
        for(int k = 0; k < size; k++){
            printf("%d\t", array[k]);
        }
        printf("\n");

    }
};


int main(){
    int array[] = {112,13,1, 36, 4,-9,549,66};
    int size = 8;
    bubble_sort(array, size);
    printf("The sorted array is :\n");
    for(int i = 0; i < size; i++){
        printf("%d\t", array[i]);
    }
    return 0;


}
