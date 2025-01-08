from src.binary_search import binary_search
import pytest

def test_finds_ele_in_list():
    nums = [2,4,6,8,10]

    assert binary_search(nums, 2) == 0
    assert binary_search(nums, 4) == 1
    assert binary_search(nums, 6) == 2
    assert binary_search(nums, 8) == 3
    assert binary_search(nums, 10) == 4


def test_returns_negative_index_when_not_found():
    nums = [2,4,6,8,10]

    assert binary_search(nums, 0) == -1
    assert binary_search(nums, 1) == -1
    assert binary_search(nums, 3) == -1
    assert binary_search(nums, 5) == -1
    assert binary_search(nums, 7) == -1
    assert binary_search(nums, 9) == -1
    assert binary_search(nums, 11) == -1

def test_list_not_mutated():
    nums = [2,4,6,8,10]

    binary_search(nums, 0) == -1
    binary_search(nums, 6) == 2

    assert nums == [2,4,6,8,10]



