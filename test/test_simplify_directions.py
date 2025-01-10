from src.simply_directions import simplify_directions
import pytest

def test_error_produced_if_invalid_list():
    input = ["north", "south", "laskjfla"]

    with pytest.raises(ValueError):
        simplify_directions(input)

def test_empty_list_returns_empty_list():
    input = []
    expected_outcome = []

    assert simplify_directions(input) == expected_outcome

def test_input_is_not_altered():
    input = ["NORTH"]
    expected_outcome = ["NORTH"]
    
    assert simplify_directions(input) is not input
    
def test_for_simple_case():
    input = ["NORTH", "SOUTH", "WEST"]
    expected_outcome = ["WEST"]

    assert simplify_directions(input) == expected_outcome
    
def test_for_complex_cases():
    input = ["NORTH", "WEST", "SOUTH", "WEST", "EAST"]
    expected_outcome = ["WEST"]

    assert simplify_directions(input) == expected_outcome

    input = ["NORTH", "EAST", "SOUTH", "WEST", "NORTH", "NORTH"]
    expected_outcome = ["NORTH", "NORTH"]

    assert simplify_directions(input) == expected_outcome