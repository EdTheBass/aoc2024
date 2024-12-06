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

def traverse_guard(map):
    rows = map.splitlines()
    start_index = map.index("^")
    shift = len(rows[0]) + 1
    row,col = start_index // shift, start_index % shift
    
    # up is [-1,0], down is [1,0], left is [0,-1], right is [0,1]
    direction = [-1,0]
    position = [row,col]
    while True:
        next_pos = [position[0] + direction[0], position[1] + direction[1]]
        p1,p2 = next_pos
        if p1 * p2 < 0 or p1 >= shift-1 or p2 >= len(rows):
            break
        if rows[p1][p2] == "#":
            direction = next_direction(direction)
            continue
        else:
            i = shift * p1 + p2
            map = map[:i] + "X" + map[i+1:]
            position = next_pos
    
    return map.count("X")
        

print(traverse_guard(puzzle_input))
