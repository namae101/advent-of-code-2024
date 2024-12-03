import re
f = open("./input/day3.txt", "r")

instruction = []

for line in f:
    instruction.append(line.strip())

regex = "(mul\(\d{1,3},\d{1,3}\))|(do\(\))|(don't\(\))"

def evaluate(match):
    left_bracket = match.find("(")
    right_bracket = match.find(")")
    comma = match.find(",")
    a = int(match[left_bracket + 1:comma])
    b = int(match[comma + 1:right_bracket])
    return a * b

def findAllInstructions(instruction:str):
    operation = []
    for match in re.finditer(regex, instruction):
        operation.append(instruction[match.start():match.end()])
    return operation    

def solution():
    total = 0
    DO = True
    for i in range(len(instruction)):
        current = instruction[i]
        matches = findAllInstructions(current)
        for match in matches:
            if "mul" in match and DO:
                total += evaluate(match)
            elif "do()" in match:
                DO = True
            elif "don't()" in match:
                DO = False
    return total

print(solution())
        