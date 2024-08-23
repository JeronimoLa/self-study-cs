
import random

"""Insertion sort can be faster than merge sort if the list not huge, 
and uses less of our servers memory when list sizes are small"""

def insertion_sort(nums):
    
    for num in range(len(nums)):
        j = num
        
        while j > 0 and nums[j-1] > nums[j]:

            nums[j], nums[j-1] = nums[j-1], nums[j]
            j-=1 
    
    return nums



def main():

    arr = []

    for i in range(random.randint(5, 20)):
        rand_num = random.randrange(1, 2000)
        arr.append(rand_num)

    print(f"\n\nORIGINAL LIST: {arr}\n\n")    
    sorted_list = insertion_sort(arr)
    print(f"SORTED LIST: {sorted_list}\n\n")


if __name__ == "__main__":
    main()
