test_input = """............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............"""

with open("input8.txt", "r") as f:
    puzzle_input = f.read()

def valid(x,y,grid):
    if x >= 0 and y >=0 and x < len(grid) and y < len(grid[0]) and grid[x][y] != "#":
        return True
    return False

def find_frequencies(data):
    freqs = {}
    lines = data.splitlines()

    for i,l in enumerate(lines):
        for j,ch in enumerate(l):
            if ch not in ("\n", "."):
                get = freqs.get(ch)
                if get is not None:
                    freqs[ch] = get + [[i,j]]
                else:
                    freqs[ch] = [[i,j]]
    
    total = 0
    for key, value in freqs.items():
        for r1,c1 in value:
            for r2,c2 in value:
                if r2 == r1 and c2 == c1:
                    continue
                dx,dy = r2 - r1, c2 - c1
                x1,y1 = r2+dx, c2+dy
                x2,y2 = r1-dx, c1-dy
                if valid(x1,y1,lines):
                    lines[x1] = lines[x1][:y1] + "#" + lines[x1][y1+1:]
                    total += 1
                if valid(x2,y2,lines):
                    lines[x2] = lines[x2][:y2] + "#" + lines[x2][y2+1:]
                    total += 1
    return total

print(find_frequencies(puzzle_input))
