import re

test_input = """xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"""

with open("input3.txt", "r") as f:
    puzzle_input = f.read()

def parse_memory(data):
    muls = re.findall(r"mul\((\d+),(\d+)\)", data)
    
    total = sum([int(x[0])*int(x[1]) for x in muls])
    
    return total

print(parse_memory(puzzle_input))
