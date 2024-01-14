/*
A C implementation of binary search 
from Grokking Algo textbook Ch1
*/


# include <stdio.h>
# include <math.h>

int binary_search(int num_list[], int size, int item){
/* 
    This functions consumes an array of integers, 
    and its size, and the item to find.
    It return the index of item if it is found,
    otherwise return -1
*/
    int low = 0;
    int high = size -1;

    while(low <= high){
        // mid consumes a float, and returns an int
        int mid = floor((low + high) / 2);
        int guess = num_list[mid];
        if (guess == item){
            return mid;
        }
        else{
            if(guess < item){
                low = mid + 1;
            }
            else{
                high = mid - 1;
            }
        }

    }
    return -1;


}

int main(){
    // observe how to define an array here
    int num_list[] = {1, 2, 3, 5, 8, 13};
    
    // need to pass the size of the array to the function
    int answer = binary_search(num_list, 6, 5);
    printf("the index is %d\n", answer); // should be 3

    int answer2 = binary_search(num_list, 6, 21);
    printf("the index is %d\n", answer2); // should be -1

    int answer3 = binary_search(num_list, 6, 13);
    printf("the index is %d\n", answer3); // should be 5


    return 0;
}
