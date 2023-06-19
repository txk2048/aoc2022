import argparse


# By using a lookup table, the search for the first
# common character in the 2 strings is O(N)
def make_lookup_table(bag):
    """Makes lookup table for bag contents.

    Returns a list of 52 elements, where the first 26 elements are the
    lowercase letters and the last 26 elements are the uppercase letters."""
    lookup = [None] * 52

    for c in bag:
        if c.isupper():
            lookup[ord(c) - ord("A") + 26] = True
        else:
            lookup[ord(c) - ord("a")] = True

    return lookup


def part1(elves):
    result = 0

    for elf in elves:
        bag1 = make_lookup_table(elf[: len(elf) // 2])
        bag2 = make_lookup_table(elf[len(elf) // 2 :])

        for i, (v1, v2) in enumerate(zip(bag1, bag2)):
            if v1 and v2:
                result += i + 1
                break

    return result


def part2(elves):
    def batched(iterable, n):
        "Batch data into tuples of length n. The last batch may be shorter."
        # batched('ABCDEFG', 3) --> ABC DEF G

        from itertools import islice

        if n < 1:
            raise ValueError("n must be at least one")
        it = iter(iterable)
        while batch := tuple(islice(it, n)):
            yield batch

    result = 0

    for elf1, elf2, elf3 in batched(elves, 3):
        bag1 = make_lookup_table(elf1)
        bag2 = make_lookup_table(elf2)
        bag3 = make_lookup_table(elf3)

        for i, (v1, v2, v3) in enumerate(zip(bag1, bag2, bag3)):
            if v1 and v2 and v3:
                result += i + 1
                break

    return result


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file", help="input file")
    args = parser.parse_args()

    with open(args.input_file) as f:
        elves = [line.strip() for line in f]

    print(f"Part 1: {part1(elves)}")
    print(f"Part 2: {part2(elves)}")


if __name__ == "__main__":
    main()
