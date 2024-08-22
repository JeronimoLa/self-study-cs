
"""
The algorithm consists of two separate functions, merge_sort and merge.

merge_sort() divides the input array into two halves, calls itself for the two halves, and then merges the two sorted halves.
The merge() function is used for merging two sorted lists back into a single sorted list. At the lowest level of recursion, the two "sorted" lists will each have a length of 1. Those single element lists will be merged into a sorted list of length two, and we can build from there.


Set i and j equal to zero. They will be used to keep track of indexes in the input lists (A and B).

Use a loop to iterate over A and B at the same time. If an element in A is less than or equal to its respective element in B, add it to the final list and increment i. Otherwise, add the item in B to the final list and increment j.

After comparing all the items, there may be some items left over in either A or B (if one of the lists is longer than the other). Add those extra items to the final list.

Return the final list."""

import random 
import time


def merge_sort(unsorted_list: list):

    if len(unsorted_list) < 2:
        return unsorted_list
    
    middle = len(unsorted_list) // 2

    first_half = unsorted_list[:middle] 
    second_half = unsorted_list[middle:]

    # print(f"FIRST HALF {first_half}\n")
    # print(f"SECOND HALF {second_half}\n")

    sorted_left_side = merge_sort(first_half)
    sorted_right_side = merge_sort(second_half)

    # print(sorted_left_side)
    # print(sorted_right_side)
    return merge(sorted_left_side, sorted_right_side)


def merge(left, right): 

    final = []
    i = 0 
    j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            final.append(left[i])
            i+=1
        else:
            final.append(right[j])
            j+=1

    while i < len(left):
        final.append(left[i])
        i+=1
    
    while j < len(right):
        final.append(right[j])
        j+=1

    return final


def main():

    arr = []

    for i in range(random.randint(50, 100)):
        rand_num = random.randrange(1, 2000)
        arr.append(rand_num)

    print(f"\n\nORIGINAL LIST: {arr}\n\n")    
    sorted_list = merge_sort(arr)
    print(f"SORTED LIST: {sorted_list}\n\n")


if __name__ == "__main__":
    main()
    