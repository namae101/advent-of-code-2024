f = open("./input/day4.txt", "r")
data = []
for line in f:
    data.append(line.strip())

def count_xmas_pattern(grid):
    rows = len(grid)
    cols = len(grid[0])
    count = 0

    for r in range(1, rows - 1):  # Start from 1 to avoid index out of bounds
        for c in range(1, cols - 1):  # Start from 1 to avoid index out of bounds
            # M S
            #  A
            # M S
            if (grid[r-1][c-1] == 'M' and grid[r][c] == 'A' and grid[r-1][c+1] == 'S' and
                grid[r+1][c-1] == 'M' and grid[r+1][c+1] == 'S'):
                count += 1
            # M M
            #  A
            # S S
            if (grid[r-1][c-1] == 'M' and grid[r][c] == 'A' and grid[r-1][c+1] == 'M' and
                grid[r+1][c-1] == 'S' and grid[r+1][c+1] == 'S'):
                count += 1

            # S M
            #  A
            # S M
            if (grid[r-1][c-1] == 'S' and grid[r][c] == 'A' and grid[r-1][c+1] == 'M' and
                grid[r+1][c-1] == 'S' and grid[r+1][c+1] == 'M'):
                count += 1
            # S S
            #  A
            # M M
            if (grid[r-1][c-1] == 'S' and grid[r][c] == 'A' and grid[r-1][c+1] == 'S' and
                grid[r+1][c-1] == 'M' and grid[r+1][c+1] == 'M'):
                count += 1

    return count

print(count_xmas_pattern(data))