from dataclasses import dataclass


class Range:
    def __init__(self, blueprint) -> None:
        self.low, self.high = tuple(int(x) for x in blueprint.split("-"))

    def part1_contains(self, other):
        return self.low <= other.low and other.high <= self.high

    def part2_contains(self, other):
        return any(
            x in range(other.low, other.high + 1)
            for x in range(self.low, self.high + 1)
        )


with open("input.txt") as f:
    pairs = [tuple(Range(x) for x in line.strip().split(",")) for line in f]

part1_total = sum(
    1 for p1, p2 in pairs if p1.part1_contains(p2) or p2.part1_contains(p1)
)

part2_total = sum(
    1 for p1, p2 in pairs if p1.part2_contains(p2) or p2.part2_contains(p1)
)

print(f"Part 1: {part1_total}")
print(f"Part 2: {part2_total}")
