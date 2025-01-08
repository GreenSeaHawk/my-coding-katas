from copy import deepcopy

'''
CHALLENGE
The maximum sum sub-list problem consists of finding the maximum sum of any sequence of consecutive 
numbers in a list of integers.

When the list is made up of only positive numbers, then the maximum sum is simply the sum of the whole 
list. If the list is made up of only negative numbers, the function should return 0 instead.

An empty list is considered to have zero greatest sum. Note that the empty list is also a valid sub-list.

If a list contains positive and negative numbers, then you will need to work out which subsequence can be 
added together to give the highest total.
'''
'''
PLAN
the list will always start and finish with a positive integer
find the largest subset where the first and last nums are positive
then work out all the subsets that hold true to this same model
check all sums splitting the list by increasing values of index
do this from left to right and right to left
then shrink the list by one positive valued index from left and right
repeat this until the list is of size 2
'''
def sub_list_sum(num_list):
    nums = deepcopy(num_list)
    # find the largest subset
    highest_value = 0
    first_pos_index = -1
    for i in range(len(nums)):
        if nums[i] > 0:
            first_pos_index = i
            break
    for i in range(len(nums) -1, -1, -1):
        if nums[i] > 0:
            last_pos_index = i
            break
    if first_pos_index == -1:
        return highest_value
    new_list = nums[first_pos_index:last_pos_index + 1]
    if sum(new_list) > highest_value:
        highest_value = sum(new_list)
    
    # sum all the values working back from the right
    for i in range(1, len(new_list)):
        if sum(new_list[:i]) > highest_value:
            highest_value = sum(new_list[:i])
    # sum all the value working back from the left
    for i in range(0, len(new_list)):
        if sum(new_list[i:]) > highest_value:
            highest_value = sum(new_list[i:])
    
    def inner_func(nums):
        nonlocal highest_value
        for i in range(1, len(nums) -1):
            if nums[i] > 0:
                first_pos_index = i
                break
        for i in range(len(nums) -2, 0, -1):
            if nums[i] > 0:
                last_pos_index = i
                break
        new_list = nums[first_pos_index:last_pos_index + 1]
        if sum(new_list) > highest_value:
            highest_value = sum(new_list)
        # sum all the values working back from the right
        for i in range(1, len(new_list)):
            if sum(new_list[:i]) > highest_value:
                highest_value = sum(new_list[:i])
        # sum all the value working back from the left
        for i in range(0, len(new_list)):
            if sum(new_list[i:]) > highest_value:
                highest_value = sum(new_list[:i])
        if len(new_list) > 2:
            inner_func(new_list)
        else:
            if sum(new_list) > highest_value:
                highest_value = sum(new_list)
    
    if len(new_list) > 2:
        inner_func(new_list)
    else:
        if sum(new_list) > highest_value:
            highest_value = sum(new_list)
    
    return highest_value


        
        


    

