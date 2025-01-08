
'''
CHALLENGE
Given a square matrix (two-dimensional list) and a x_start_index and a y_start_index, you must 
return a 3 * 3 subsquare from the list.

For example, in the following matrix, if asked for the subsquare with start indexes of 0, 0, 
you would extract a two-dimensional matrix beginning from the top left-hand corner of the matrix:

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

get_sub_square(matrix, 0, 0)

# --> [[5, 3, 4], [6, 7, 2], [1, 9, 8]]
Here is another example:

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
get_sub_square(matrix, 2, 5)

# --> [[3, 9, 2], [1, 5, 3], [7, 4, 1]]
Testing Notes:
You can assume the matrix will always be square and will always have dimensions of at least 3 * 3.
If y_start_index or x_start_index is too high and a complete 3 * 3 subsquare cannot be extracted, 
the function should return a matrix with None in the overflowed positions.
'''