f = open("./input/day1.txt", "r")

left_array = []
right_array = []

for line in f:
    splitted_input = line.strip().split("   ")
    left_array.append(int(splitted_input[0], 10))
    right_array.append(int(splitted_input[1], 10))

sorted_left_array = sorted(left_array)
sorted_right_array = sorted(right_array)
total_diff = 0

for i in range(len(sorted_left_array)):
    total_diff += abs(sorted_left_array[i] - sorted_right_array[i])

print(total_diff)
