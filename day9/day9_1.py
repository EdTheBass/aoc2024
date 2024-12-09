import re
import time as t

test_input = """2333133121414131402"""

with open("input9.txt", "r") as f:
    puzzle_input = f.read()

def blockify(line):
    block = ""
    for i,ch in enumerate(line):
        if i % 2 == 0:
            block += (str(i//2) + "#") * int(ch)
        else:
            block += "." * int(ch)
    
    total = 0
    files = "".join(line[::2])
    space = "".join(line[1::2])
    
    for i,s in enumerate(space):    
        for n in range(int(s)):
            total += n * (len(files)-1)
            last_num = int(files[-1])-1
            if last_num:
                files = files[:-1] + str(last_num)
            else:
                files = files[:-1]

    return total + sum()
    
print(blockify(test_input))
