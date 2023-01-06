def is_touching(position1, position2):
    x, y = position1

    candidate_positions = []

    candidate_positions.append((x, y + 1))  # up
    candidate_positions.append((x, y - 1))  # down
    candidate_positions.append((x - 1, y))  # left
    candidate_positions.append((x + 1, y))  # right

    candidate_positions.append((x - 1, y + 1))  # up left
    candidate_positions.append((x + 1, y + 1))  # up right
    candidate_positions.append((x - 1, y - 1))  # down left
    candidate_positions.append((x + 1, y - 1))  # down right

    return any(position == position2 for position in candidate_positions)


def get_new_tail_position(new_head, current_tail):
    # no change
    if is_touching(new_head, current_tail):
        return current_tail

    head_x, head_y = new_head
    tail_x, tail_y = current_tail

    move_count = 1

    # diagonal (not same column and row)
    if head_x != tail_x and head_y != tail_y:
        move_count = 2

    # left/right
    if head_x < tail_x and move_count > 0:
        tail_x -= 1
    elif tail_x < head_x and move_count > 0:
        tail_x += 1

    # up/down
    if head_y > tail_y and move_count > 0:
        tail_y += 1
    elif tail_y > head_y and move_count > 0:
        tail_y -= 1

    return tail_x, tail_y


with open("input.txt") as f:
    instructions = [line.strip() for line in f]

head = (0, 0)
tail = (0, 0)
visited_positions = {tail}

for instruction in instructions:
    parts = instruction.split()
    dir_, count = parts[0], int(parts[1])

    for _ in range(count):
        x, y = head

        # move head
        if dir_ == "U":
            y += 1
        elif dir_ == "D":
            y -= 1
        elif dir_ == "R":
            x += 1
        else:  # dir_ == "L"
            x -= 1

        head = (x, y)
        tail = get_new_tail_position(head, tail)

        visited_positions.add(tail)


print(f"Part 1: {len(visited_positions)}")

rope_parts = [(0, 0) for _ in range(10)]
visited_positions = {rope_parts[-1]}

for instruction in instructions:
    parts = instruction.split()
    dir_, count = parts[0], int(parts[1])

    for _ in range(count):
        x, y = rope_parts[0]

        # move head
        if dir_ == "U":
            y += 1
        elif dir_ == "D":
            y -= 1
        elif dir_ == "R":
            x += 1
        else:  # dir_ == "L"
            x -= 1

        rope_parts[0] = (x, y)
        for i in range(1, 10):
            rope_parts[i] = get_new_tail_position(rope_parts[i - 1], rope_parts[i])

        visited_positions.add(rope_parts[-1])

print(f"Part 2: {len(visited_positions)}")
