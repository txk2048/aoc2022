import argparse
from dataclasses import dataclass


@dataclass
class Range:
    lower: int
    upper: int

    @staticmethod
    def from_str(s: str) -> "Range":
        lower, upper = map(int, s.split("-"))
        return Range(lower, upper)

    def __contains__(self, other: "Range") -> bool:
        return (
            self.lower <= other.lower <= self.upper
            and self.lower <= other.upper <= self.upper
        )

    def overlaps(self, other: "Range") -> bool:
        return (
            self.lower <= other.lower <= self.upper
            or self.lower <= other.upper <= self.upper
        )


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file", help="input file")
    args = parser.parse_args()

    result1 = 0
    result2 = 0

    with open(args.input_file) as f:
        for line in f:
            first, second = map(Range.from_str, line.strip().split(","))

            result1 += first in second or second in first
            result2 += first.overlaps(second) or second.overlaps(first)

    print(f"Part 1: {result1}")
    print(f"Part 2: {result2}")


if __name__ == "__main__":
    main()
