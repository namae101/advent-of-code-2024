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
fixed_updates = []

def check_valid(update):
    current_rule = rule[update[0]]
    valid = True
    for i in range(1, len(update)):
        if update[i] not in current_rule:
            valid = False
            break
        else:
            current_rule = rule[update[i]]
    return valid

def is_fit_rule(update, rule, number):
    for i in range(len(update)):
        if update[i] == number:
            continue
        if update[i] not in rule:
            return False
    return True


for update in updates:
    current_rule = rule[update[0]]
    valid = check_valid(update)
    middle = len(update) // 2
    if valid:
        continue
    # Fixing the update
    temp_update = update.copy()
    for i in range(len(temp_update)):
        best_rule = None
        best_index = None
        number = None
        for j in range(i , len(temp_update)):
            fit_rule =  is_fit_rule(temp_update[i:], rule[temp_update[j]], temp_update[j])
            if fit_rule:
                best_rule = rule[temp_update[j]]
                best_index = j
                number =  temp_update[j]
        
        temp = temp_update[i]
        temp_update[i] = temp_update[best_index]
        temp_update[best_index] = temp
    fixed_updates.append(temp_update)
    sum_middle += temp_update[middle]
    print(temp_update,check_valid(temp_update))
print(sum_middle)