from copy import deepcopy
import collections

'''
CHALLENGE
Create a function called find_most_repeated that looks through a flat list and returns a dictionary that
describes the most repeated element or elements in the list.

The dictionary will be in the format:
{"elements": ["foo"], "repeats": 3}

Example:
find_most_repeated(["foo", "foo", 1, 2, 3, "bar", 2, 3, 4, "bar", "bar", "foo"])
# {"elements": ["foo", "bar"], "repeats": 3}
'''
'''
PLAN
Check if list is empty.
Find the frequency of each element in the list.
Find the max frequency and if greater than 1 then set the output dict
values to be the most frequent items and the frequency of the repeat.
'''

def find_most_repeated(elements):
    c_elements = deepcopy(elements)
    output_dict = {"elements": [], "repeats": None}
    if len (c_elements) == 0:
        return output_dict
    counter_dict = dict(collections.Counter(c_elements))
    frequency_of_most_common_ele = max(counter_dict.values())
    if frequency_of_most_common_ele > 1:
        output_dict["elements"] = [k for k,v in counter_dict.items() if v == frequency_of_most_common_ele]    
        output_dict["repeats"] = frequency_of_most_common_ele
    return output_dict
