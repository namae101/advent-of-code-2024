f = open("./input/day1.txt", "r")

left_array = []
right_array = []

for line in f:
    splitted_input = line.strip().split("   ")
    left_array.append(int(splitted_input[0], 10))
    right_array.append(int(splitted_input[1], 10))

right_count = {}
for i in right_array:
    if i in right_count:
        right_count[i] += 1
    else:
        right_count[i] = 1

similarity_score = 0
for i in left_array:
    if i in right_count:
        similarity_score += i * right_count[i]
print(similarity_score)