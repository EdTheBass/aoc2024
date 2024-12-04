import numpy as np

test_input = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX"""

with open("input4.txt", "r") as f:
    puzzle_input = f.read()

def count(d):
    return d.count("XMAS") + d.count("SAMX")

def find_xmas(grid):
    lines = grid.splitlines()
    sideways = "\n".join(["".join([x[i] for x in lines]) for i in range(len(lines))])
    s_lines = sideways.splitlines()
    diagonal1 = "\n".join(["".join([x[i+j] for j,x in enumerate(lines[:len(lines)-i])]) for i in range(len(lines)-1)])
    diagonal2 = "\n".join(["".join([x[i+j] for j,x in enumerate(s_lines[:len(s_lines)-i])]) for i in range(len(s_lines)-1)][1:])
    diagonal3 = "\n".join(["".join([x[i+j] for j,x in enumerate(lines[::-1][:len(lines)-i])]) for i in range(len(s_lines)-1)])    
    diagonal4 = "\n".join(["".join([x[::-1][i+j] for j,x in enumerate(s_lines[:len(lines)-i])]) for i in range(len(s_lines)-1)][1:])
    
    horizontal = count(grid)
    vertical = count(sideways)
    diagonal = count(diagonal1) + count(diagonal2) + count(diagonal3) + count(diagonal4)

    return horizontal + vertical + diagonal


print(find_xmas(puzzle_input))
