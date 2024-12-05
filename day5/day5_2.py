import re

test_input = """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47"""

with open("input5.txt", "r") as f:
    puzzle_input = f.read()

def is_valid(update, rules):
    for i,num1 in enumerate(update):
        for num2 in update[:i]:
            get = rules.get(num1)
            if get is not None:
                if num2 in get: return False, [num1,num2]
    return True, []

def dictify(rules):
    rule_dict = {}
    for pair in rules:
        n1,n2 = pair
        get = rule_dict.get(n1)
        if not get:
            rule_dict[n1] = [n2]
        else:
            rule_dict[n1] = get + [n2]
    return rule_dict


def update_count(text):
    ordering_rules = dictify([[int(x[0]), int(x[1])] for x in re.findall(r"(\d*)\|(\d*)", text)])
    split = text.splitlines()
    updates = [[int(x) for x in y.split(",")] for y in split[split.index("")+1:]]

    total = 0
    to_fix = []
    swaps = []
    for upd in updates:
        valid, swap = is_valid(upd, ordering_rules)
        if not valid:
            swaps.append(swap)
            to_fix.append(upd)

    for i,f in enumerate(to_fix):
        new_f = f[:]
        valid = False
        curr_swap = swaps[i]
        while not valid:
            s1,s2 = curr_swap
            i1,i2 = new_f.index(s1), new_f.index(s2)
            new_f[i1],new_f[i2] = new_f[i2],new_f[i1]
            valid,curr_swap = is_valid(new_f, ordering_rules)
        
        total += new_f[len(new_f)//2]

    return total


print(update_count(puzzle_input))
