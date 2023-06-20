import argparse
import copy
from dataclasses import dataclass
import json
import re
from typing import List, Self


INSTRUCTION_PATTERN = re.compile(r"^move (\d+) from (\d+) to (\d+)$")


@dataclass
class Instruction:
    amount: int
    source: int
    target: int

    @staticmethod
    def from_str(s: str) -> Self:
        m = INSTRUCTION_PATTERN.match(s)
        if not m:
            raise ValueError(f"Invalid instruction: {s}")

        amount, source, target = map(int, m.groups())

        return Instruction(amount, source, target)


def part1(starting_stacks: List[List[str]], instructions: List[Instruction]) -> str:
    stacks = copy.deepcopy(starting_stacks)

    for instruction in instructions:
        for _ in range(instruction.amount):
            stacks[instruction.target - 1].append(stacks[instruction.source - 1].pop())

    return "".join(stack[-1] for stack in stacks)


def part2(starting_stacks: List[List[str]], instructions: List[Instruction]) -> str:
    stacks = copy.deepcopy(starting_stacks)

    for instruction in instructions:
        stacks[instruction.target - 1] += stacks[instruction.source - 1][
            -instruction.amount :
        ]

        del stacks[instruction.source - 1][-instruction.amount :]

    return "".join(stack[-1] for stack in stacks)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file", help="input file")
    args = parser.parse_args()

    with open(args.input_file) as f:
        data = json.load(f)

    starting_stacks = data["starting_stacks"]
    instructions = list(map(Instruction.from_str, data["instructions"]))

    print(f"Part 1: {part1(starting_stacks, instructions)}")
    print(f"Part 2: {part2(starting_stacks, instructions)}")


if __name__ == "__main__":
    main()
