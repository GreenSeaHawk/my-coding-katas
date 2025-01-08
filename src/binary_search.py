from copy import deepcopy

'''
CHALLENGE
The goal of this kata is to implement a function that searches for a number in a list and returns its index,
or -1 if it's not found. Essentially, the same functionality as list.index.

You should implement this functionality using a binary search algorithm. Binary search is a very common 
algorithm for searching ordered lists. An example of this algorithm would be searching for the Northcoders 
phone number in the phonebook:

You open the phonebook in half and see what letter you're on.
If it's a letter previous to 'N', you discard all the pages on your left and keep searching on your right.
You open the remaining pages in half and see what letter you're on. If it's a letter after 'N', you discard 
the pages on your right and keep searching on the pages on your left.
Repeat the process until there's only one page left.
You can assume that the list passed to the function will always be ordered and have unique, numeric values.
'''

def binary_search(num_list, ele):
    nums = deepcopy(num_list)
    middle_index = int(len(nums) / 2)
    index = -1
    def inner_func(new_list, ele):
        nonlocal index, middle_index
        banked_index = 0
        while len(new_list) > 0:
            if ele == new_list[middle_index]:
                index = middle_index
                index += banked_index
                break
            elif ele > new_list[middle_index]:
                new_list = new_list[middle_index + 1:]
                banked_index += middle_index + 1
                middle_index = int(len(new_list) / 2)
                inner_func(new_list, ele)
            else:
                new_list = new_list[:middle_index]
                middle_index = int(len(new_list) / 2)
                inner_func(new_list, ele)
    inner_func(nums, ele)
    return index
        
