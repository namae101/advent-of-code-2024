f = open("./input/day5.txt", "r")
rule = {}
updates = []
read_rule = True
for line in f:
    if len(line.strip()) == 0:
        read_rule = False
        continue
    # Reading Rule
    if read_rule:
        [left, right] = [int(x,10) for x in line.strip().split("|")]
        if left not in rule:
            rule[left] = [right]
        else:
            rule[left].append(right)
    # Reading Update
    if not read_rule:
        updates.append([int(x,10) for x in line.strip().split(",")])

valid_count = 0
sum_middle = 0
for update in updates:
    current_rule = rule[update[0]]
    valid = True
    middle = len(update) // 2
    for i in range(1, len(update)):
        if update[i] not in current_rule:
            valid = False
            break
        else:
            current_rule = rule[update[i]]
    if valid:
        valid_count += 1
        sum_middle += update[middle]
print(valid_count)
print(sum_middle)
    
