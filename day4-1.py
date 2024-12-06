f = open("./input/day4.txt", "r")
data = []
for line in f:
    data.append(line.strip())
    
def count_xmas(grid):
    word = "XMAS"
    rows = len(grid)
    cols = len(grid[0])
    count = 0

    # Directions: (row_offset, col_offset)
    directions = [
        (0, 1),   # right
        (0, -1),  # left
        (1, 0),   # down
        (-1, 0),  # up
        (1, 1),   # down-right
        (-1, -1), # up-left
        (1, -1),  # down-left
        (-1, 1)   # up-right
    ]

    for r in range(rows):
        for c in range(cols):
            for dr, dc in directions:
                # Check if we can find "XMAS" in this direction
                found = True
                for i in range(len(word)):
                    nr = r + dr * i
                    nc = c + dc * i
                    if nr < 0 or nr >= rows or nc < 0 or nc >= cols or grid[nr][nc] != word[i]:
                        found = False
                        break
                if found:
                    count += 1

    return count


print(count_xmas(data))