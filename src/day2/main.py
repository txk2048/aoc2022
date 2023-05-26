import argparse
import enum
from typing import Self


class Move(enum.Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

    @staticmethod
    def from_str(move_str: str) -> Self:
        if move_str == "A" or move_str == "X":
            return Move.ROCK
        elif move_str == "B" or move_str == "Y":
            return Move.PAPER
        elif move_str == "C" or move_str == "Z":
            return Move.SCISSORS

        raise ValueError(f"Invalid move string: {move_str}")

    @staticmethod
    def from_result(opponent_move: Self, result: "Result") -> Self:
        if result == Result.DRAW:
            return opponent_move
        elif result == Result.WIN:
            if opponent_move == Move.ROCK:
                return Move.PAPER
            elif opponent_move == Move.PAPER:
                return Move.SCISSORS
            elif opponent_move == Move.SCISSORS:
                return Move.ROCK
        elif result == Result.LOSE:
            if opponent_move == Move.ROCK:
                return Move.SCISSORS
            elif opponent_move == Move.PAPER:
                return Move.ROCK
            elif opponent_move == Move.SCISSORS:
                return Move.PAPER

        raise ValueError(f"Invalid result: {result}")


class Result(enum.Enum):
    WIN = 6
    LOSE = 0
    DRAW = 3

    @staticmethod
    def from_str(result_str: str) -> Self:
        if result_str == "X":
            return Result.LOSE
        elif result_str == "Y":
            return Result.DRAW
        elif result_str == "Z":
            return Result.WIN

        raise ValueError(f"Invalid result string: {result_str}")

    @staticmethod
    def from_move(opponent_move: Move, player_move: Move) -> Self:
        if opponent_move == player_move:
            return Result.DRAW
        elif opponent_move == Move.ROCK and player_move == Move.PAPER:
            return Result.WIN
        elif opponent_move == Move.PAPER and player_move == Move.SCISSORS:
            return Result.WIN
        elif opponent_move == Move.SCISSORS and player_move == Move.ROCK:
            return Result.WIN

        return Result.LOSE


def part1(rounds):
    score = 0

    for round_ in rounds:
        opponent, player = round_
        opponent_move, player_move = Move.from_str(opponent), Move.from_str(player)
        round_result = Result.from_move(opponent_move, player_move)

        score += round_result.value
        score += player_move.value

    return score


def part2(rounds):
    score = 0

    for round_ in rounds:
        opponent, result = round_
        opponent_move = Move.from_str(opponent)

        target_result = Result.from_str(result)
        player_move = Move.from_result(opponent_move, target_result)

        score += target_result.value
        score += player_move.value

    return score


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file", help="input file")
    args = parser.parse_args()

    with open(args.input_file) as f:
        rounds = [tuple(line.strip().split()) for line in f]

    print(f"Part 1: {part1(rounds)}")
    print(f"Part 2: {part2(rounds)}")


if __name__ == "__main__":
    main()
