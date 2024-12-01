import numpy as np
import re

test_input = """3   4
4   3
2   5
1   3
3   9
3   3"""

with open("input1.txt", "r") as f:
    puzzle_input = f.read()

def parse_list(lists):
    rows = lists.splitlines()
    list1,list2 = [], []

    for row in rows:
        nums = re.search(r"([0-9]+) *([0-9]+)", row)
        list1.append(int(nums.group(1)))
        list2.append(int(nums.group(2)))

    total = 0
    for num in list1:
        total += num * list2.count(num)
    
    return total

print(parse_list(test_input))
