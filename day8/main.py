def is_visible(grid: list[list[int]], row: int, col: int) -> bool:
    left = grid[row][0:col]  # cells to the left
    right = grid[row][col + 1 :]  # cells to the right
    up = [grid[y][col] for y in range(row)]  # cells above
    down = [grid[y][col] for y in range(row + 1, len(grid))]  # cells below

    for line in (left, right, up, down):
        # check if any tree is at least as tall as this one
        if not any(tree >= grid[row][col] for tree in line):
            return True  # there is no tree blocking this one

    return False


def scenic_score(grid: list[list[int]], row: int, col: int) -> int:
    left = grid[row][0:col]  # cells to the left in inside to outside order
    left.reverse()

    right = grid[row][col + 1 :]  # cells to the right in inside to outside order

    up = [grid[y][col] for y in range(row)]  # cells above in inside to outside order
    up.reverse()

    down = [
        grid[y][col] for y in range(row + 1, len(grid))
    ]  # cells below in inside to outside order

    score = 1
    for line in (left, right, up, down):
        # the count of trees we can see
        count = 0

        for tree in line:
            count += 1

            # we have found the first tree that is this height or taller
            if tree >= grid[row][col]:
                break

        score *= count

    return score


with open("input.txt") as f:
    grid = [[int(c) for c in line.strip()] for line in f]

visible_count = 0
for row_index, row in enumerate(grid):
    for col_index, _ in enumerate(row):
        if is_visible(grid, row_index, col_index):
            visible_count += 1

print(f"Part 1: {visible_count}")

result = 0
for row_index, row in enumerate(grid):
    for col_index, _ in enumerate(row):
        score = scenic_score(grid, row_index, col_index)
        result = max(result, score)

print(f"Part 2: {result}")
