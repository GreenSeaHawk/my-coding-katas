from src.sub_list_sum import sub_list_sum

def test_list_not_mutated():
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    
    sub_list_sum(nums)

    assert nums == [-2, 1, -3, 4, -1, 2, 1, -5, 4]

def test_sums_correctly_1():
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

    assert sub_list_sum(nums) == 6

def test_sums_correctly_2():
    nums = [9, 8, 7, -3, 6, 5, 4, -3, 2, 1]

    assert sub_list_sum(nums) == 36
    
def test_sums_correctly_3():
    nums = [5, -6, 2, 9, -4, -3, 8, -10, 20]

    assert sub_list_sum(nums) == 22

def test_returns_0_for_all_negative():
    nums = [-1,-2,-3]

    assert sub_list_sum(nums) == 0

def test_returns_0_for_empty_list():
    nums = []

    assert sub_list_sum(nums) == 0
