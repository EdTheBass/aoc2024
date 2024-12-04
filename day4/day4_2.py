import re

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
    count1 = len(re.findall(r"(?=(M.S[\S\s]{139}A[\S\s]{139}M.S))", d))
    count2 = len(re.findall(r"(?=(S.M[\S\s]{139}A[\S\s]{139}S.M))", d))
    count3 = len(re.findall(r"(?=(S.S[\S\s]{139}A[\S\s]{139}M.M))", d))
    count4 = len(re.findall(r"(?=(M.M[\S\s]{139}A[\S\s]{139}S.S))", d))
    return count1 + count2 + count3 + count4
    

def find_xmas(grid):
    return count(grid)


print(find_xmas(puzzle_input))
