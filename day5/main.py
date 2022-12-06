import copy
import json
import re

with open("input.json") as f:
    data = json.load(f)
    stacks1: list[list[str]] = data["stacks"]
    stacks2 = copy.deepcopy(stacks1)

    instructions: list[str] = data["instructions"]

# part 1
for instruction in instructions:
    m = re.match(r"^move (\d+) from (\d+) to (\d+)$", instruction.strip())
    count = int(m[1])
    src = int(m[2]) - 1
    dest = int(m[3]) - 1

    for _ in range(count):
        stacks1[dest].append(stacks1[src].pop())

message1 = "".join(stack[-1] for stack in stacks1)
print(f"Part 1: {message1}")

# part 2
for instruction in instructions:
    m = re.match(r"^move (\d+) from (\d+) to (\d+)$", instruction.strip())
    count = int(m[1])
    src = int(m[2]) - 1
    dest = int(m[3]) - 1

    buffer = []
    for _ in range(count):
        buffer.append(stacks2[src].pop())

    while buffer:
        stacks2[dest].append(buffer.pop())

message2 = "".join(stack[-1] for stack in stacks2)
print(f"Part 2: {message2}")
