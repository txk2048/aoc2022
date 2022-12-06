import string
import itertools


def chunk(arr, chunk_size):
    # https://www.geeksforgeeks.org/break-list-chunks-size-n-python/
    arr = iter(arr)
    return iter(lambda: tuple(itertools.islice(arr, chunk_size)), ())


def score_from_item(item):
    return 1 + string.ascii_lowercase.find(item.lower()) + (26 if item.isupper() else 0)


with open("input.txt") as f:
    bags = [line.strip() for line in f]

part1_score = 0
for bag in bags:
    first, second = bag[0 : len(bag) // 2], bag[len(bag) // 2 :]

    repeat = None
    for item in first:
        if item in second:
            repeat = item
            break

    part1_score += score_from_item(repeat)


part2_score = 0
for bag1, bag2, bag3 in chunk(bags, 3):
    repeat = None
    for item in bag1:
        if item in bag2 and item in bag3:
            repeat = item
            break

    part2_score += score_from_item(repeat)

print(f"Part 1: {part1_score}")
print(f"Part 2: {part2_score}")
