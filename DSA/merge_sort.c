

#include<stdio.h>


void printArray(int array[], int size){

    for(int i=0; i<size; i++)
        printf("%d ", array[i]);
    printf("\n");

}


int* merge_sort(int array[], int size){

    if (size < 2){
        return array;
    }

    int middle = size / 2;
    int hello = 5;
    printf("%d", middle);
    printf("%d", hello);
    

    return 0;
}


int main(){
    // driver code 
    int arr[] = {4, 10};
    int arr_size = sizeof(arr) / sizeof(arr[0]);

    printf("Original Array: ");
    printArray(arr, arr_size);

    int* sorted = merge_sort(arr, arr_size);

    printArray(sorted, arr_size);


    return 0;
}


// Creat a function that can generating an array of size 100000 plus and sort using the merge_sort algorithm, and do that ten times and measure performance
