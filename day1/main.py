with open("input.txt") as f:
    elves_calories = []  # list of the calories of all elves
    elf_calories = 0  # running sum of the calories of the current elf

    for line in f:
        line = line.strip()
        if line == "":
            elves_calories.append(elf_calories)
            elf_calories = 0
        else:
            elf_calories += int(line)

    # handle last elf
    elves_calories.append(elf_calories)
    elves_calories.sort(reverse=True)

print(f"Part 1: {elves_calories[0]}")
print(f"Part 2: {sum(elves_calories[0:3])}")
