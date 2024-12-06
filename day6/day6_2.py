test_input = """....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#..."""

with open("input6.txt", "r") as f:
    puzzle_input = f.read()

def next_direction(direction):
    dirs = {(-1,0): (0,1), (1,0): (0,-1), (0,-1): (-1,0), (0,1): (1,0)}
    return dirs.get(tuple(direction))

def has_loop(map, empty):
    rows = map.splitlines()
    start_index = map.index("^")
    shift = len(rows[0]) + 1
    row,col = start_index // shift, start_index % shift
    
    # up is [-1,0], down is [1,0], left is [0,-1], right is [0,1]
    direction = [-1,0]
    position = [row,col]
    visited = 0
    while True:
        next_pos = [position[0] + direction[0], position[1] + direction[1]]
        p1,p2 = next_pos
        if p1 * p2 < 0 or p1 >= shift-1 or p2 >= len(rows):
            return False
        if rows[p1][p2] == "#":
            direction = next_direction(direction)
            continue
        else:
            if visited > empty:
                return True
            
            visited += 1
            position = next_pos
        
def find_obstructions(map):
    total = 0
    empty = map.count(".")
    for i,m in enumerate(map):
        if m == ".":
            map = map[:i] + "#" + map[i+1:]
            if has_loop(map, empty-1):
                total += 1
            map = map[:i] + "." + map[i+1:]
    return total

print(find_obstructions(puzzle_input))
