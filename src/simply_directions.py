from copy import deepcopy
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

def simplify_directions(directs):
    dirs = deepcopy(directs)
    count = {"NORTH": 0, "WEST": 0, "SOUTH": 0, "EAST": 0}
    new_dirs = []
    for dir in dirs:
        if dir not in count.keys():
            raise ValueError("Invalid list of directions")
        if dir in count.keys():
            count[dir] += 1
    ns_count = count["NORTH"] - count["SOUTH"]
    ew_count = count["EAST"] - count ["WEST"]

    if ns_count > 0:
        for _ in range(ns_count):
            new_dirs.append("NORTH")
    if ns_count < 0:
        for _ in range(-ns_count):
            new_dirs.append("SOUTH")
    if ew_count > 0:
        for _ in range(ew_count):
            new_dirs.append("EAST")
    if ew_count < 0:
        for _ in range(-ew_count):
            new_dirs.append("WEST")

    return new_dirs