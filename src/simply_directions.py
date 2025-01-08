
'''
CHALLENGE
The challenge is to implement a function that takes a list of directions and simplifies them. 
Directions can be simplified if any two directions cause the person to end up in the same place. 
For example, the directions ["NORTH", "SOUTH"] cancel one another out and the function should 
return an empty list of no directions [].

Examples
simplify_directions(["NORTH", "SOUTH", "WEST"])
# --> ["WEST"]
simplify_directions(["NORTH", "WEST", "SOUTH", "WEST", "EAST"])
# --> ["WEST"]
simplify_directions(["NORTH", "EAST", "SOUTH", "WEST", "NORTH", "NORTH"])
# --> ["NORTH", "NORTH"]
'''