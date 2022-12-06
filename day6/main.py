with open("input.txt") as f:
    buffer = f.read().strip()

for i in range(len(buffer) - 3):
    data = buffer[i : i + 4]
    if len(set(data)) == 4:
        print(f"Part 1: {i + 4}")
        break

for i in range(len(buffer) - 13):
    data = buffer[i : i + 14]
    if len(set(data)) == 14:
        print(f"Part 2: {i + 14}")
        break
