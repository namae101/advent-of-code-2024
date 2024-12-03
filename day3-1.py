import re
f = open("./input/day3.txt", "r")

instruction = []

for line in f:
    instruction.append(line.strip())
total = 0

regex = "mul\(\d{1,3},\d{1,3}\)"

for i in range(len(instruction)):
    current = instruction[i]
    matches = re.findall(regex, current)
    for match in matches:
        left_bracket = match.find("(")
        right_bracket = match.find(")")
        comma = match.find(",")
        a = int(match[left_bracket + 1:comma])
        b = int(match[comma + 1:right_bracket])
        total += a * b
print(total)