from copy import deepcopy
nums = [2,4,6,-8,-10,12]
print(nums[0:])
print(nums[1:])
print(nums[len(nums)-1:])


print([i for i in range(len(nums) -1, -1, -1)])
def sub_list_sum(num_list):
    nums = deepcopy(num_list)
    # find first positive number
    
    for i in range(len(nums)):
        if nums[i] > 0:
            first_pos_index = i
            break
    for i in range(len(nums) -1, -1, -1):
        if nums[i] > 0:
            last_pos_index = i
            break
    new_list = nums[first_pos_index:last_pos_index + 1]
    highest_value = sum(new_list)
    def inner_func(nums):
        nonlocal highest_value
        for i in range(1, len(nums)):
            if nums[i] > 0:
                first_pos_index = i
                break
        for i in range(len(nums) -2, 0, -1):
            if nums[i] > 0:
                last_pos_index = i
                break
        if first_pos_index:

            new_list = nums[first_pos_index:last_pos_index + 1]
            new_highest_value = sum(new_list)
            if new_highest_value > highest_value:
                highest_value = new_highest_value
            inner_func(new_list)
        
    return highest_value

# print(sub_list_sum(nums))


