from src.get_sub_square import get_sub_square
import pytest

def test_raises_error_if_matrix_too_small():
    matrix = [[0,0,0],[0,0,0]]
    xsi = 0
    ysi = 0

    with pytest.raises(ValueError):
        get_sub_square(matrix, xsi, ysi)
    
    matrix = [[0,0],[0,0],[0,0]]
    xsi = 0
    ysi = 0

    with pytest.raises(ValueError):
        get_sub_square(matrix, xsi, ysi)

def test_raises_error_if_start_points_not_in_matrix():
    matrix = [[0,0,0],[0,0,0],[0,0,0]]
    xsi = 0
    ysi = 3

    with pytest.raises(ValueError):
        get_sub_square(matrix, xsi, ysi)

    matrix = [[0,0,0],[0,0,0],[0,0,0]]
    xsi = 3
    ysi = 0

    with pytest.raises(ValueError):
        get_sub_square(matrix, xsi, ysi)

def test_correct_matrix_with_entire_matrix_not_none_small():
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    xsi = 0
    ysi = 0

    assert get_sub_square(matrix,xsi,ysi) == [[1,2,3],[4,5,6],[7,8,9]]

def test_correct_matrix_with_entire_matrix_not_none_large():
    matrix = [
    [5, 3, 4, 6, 7, 8, 9, 1, 2],
    [6, 7, 2, 1, 9, 5, 3, 4, 8],
    [1, 9, 8, 3, 4, 2, 5, 6, 7],
    [8, 5, 9, 7, 4, 1, 4, 2, 3],
    [4, 2, 6, 8, 5, 3, 7, 9, 1],
    [7, 1, 3, 9, 2, 4, 8, 5, 6],
    [9, 6, 1, 5, 3, 7, 2, 8, 4],
    [2, 8, 7, 4, 1, 9, 6, 3, 5],
    [3, 4, 5, 2, 8, 6, 1, 7, 9]
]
    xsi = 2
    ysi = 5

    assert get_sub_square(matrix,xsi,ysi) == [[3, 9, 2], [1, 5, 3], [7, 4, 1]]

def test_correct_matrix_when_some_values_are_none():
    matrix = [
    [5, 3, 4, 6, 7, 8, 9, 1, 2],
    [6, 7, 2, 1, 9, 5, 3, 4, 8],
    [1, 9, 8, 3, 4, 2, 5, 6, 7],
    [8, 5, 9, 7, 4, 1, 4, 2, 3],
    [4, 2, 6, 8, 5, 3, 7, 9, 1],
    [7, 1, 3, 9, 2, 4, 8, 5, 6],
    [9, 6, 1, 5, 3, 7, 2, 8, 4],
    [2, 8, 7, 4, 1, 9, 6, 3, 5],
    [3, 4, 5, 2, 8, 6, 1, 7, 9]
]
    xsi = 7
    ysi = 7

    assert get_sub_square(matrix,xsi,ysi) == [[3,5,None],[7,9,None],[None,None,None]]

