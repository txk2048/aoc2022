import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file", help="input file")
    args = parser.parse_args()

    with open(args.input_file) as f:
        elves = []
        current_elf = 0

        for line in f:
            line = line.strip()

            if line == "":
                elves.append(current_elf)
                current_elf = 0
            else:
                current_elf += int(line)

    elves.sort()

    print(f"Part 1: {elves[-1]}")
    print(f"Part 2: {sum(elves[-3:])}")


if __name__ == "__main__":
    main()
