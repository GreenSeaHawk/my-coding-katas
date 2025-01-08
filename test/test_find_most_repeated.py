from src.find_most_repeated import find_most_repeated
import pytest

# @pytest.mark.skip
def test_empty_list_returns_no_repeats():
    input = []
    outcome = {"elements": [], "repeats": None}

    assert find_most_repeated(input) == outcome

# @pytest.mark.skip
def test_input_list_is_not_mutated():
    input = ["foo", "bar", "hello", "world"]
    outcome = {"elements": [], "repeats": None}
    
    find_most_repeated(input)

    assert input == ["foo", "bar", "hello", "world"] 

# @pytest.mark.skip
def test_no_repeats_list_returns_no_repeats():
    input = ["foo", "bar", "hello", "world"]
    outcome = {"elements": [], "repeats": None}

    assert find_most_repeated(input) == outcome

# @pytest.mark.skip
def test_1_repeat_list_returns_correct_repeat():
    input = ["foo", "foo", "bar", "hello", "world"]
    outcome = {"elements": ["foo"], "repeats": 2}

    assert find_most_repeated(input) == outcome

# @pytest.mark.skip
def test_2_repeats_list_returns_correct_2_repeats():
    input = ["foo", "foo", 1, 2, 3, "bar", 2, 3, 4, "bar", "bar", "foo"]
    outcome = {"elements": ["foo", "bar"], "repeats": 3}

    assert find_most_repeated(input) == outcome
