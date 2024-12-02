import re

test_input = """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9"""

with open("input2.txt", "r") as f:
    puzzle_input = f.read()

def safety(row, k=-1):
    numbers = re.findall(r"\d+", row)

    if k == 5:
        return 0
    elif k >= -1:
        numbers.pop(k)

    common_difference = [int(numbers[i+1])-int(numbers[i]) for i in range(len(numbers)-1)]
    _min,_max = min(common_difference),max(common_difference)
    if max(abs(_min), _max) > 3 or _min*_max <= 0:
        return safety(row,k=k+1)
    return 1

def determine_safety(data):
    rows = data.splitlines()

    safe = 0
    for row in rows:
        safe += safety(row)

    return safe


print(determine_safety(puzzle_input))
