from enum import Enum


class RoundResult(Enum):
    LOSE = 0
    DRAW = 3
    WIN = 6

    @staticmethod
    def from_str(s: str):
        if s == "X":
            return RoundResult.LOSE
        elif s == "Y":
            return RoundResult.DRAW
        elif s == "Z":
            return RoundResult.WIN


class Move(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

    @staticmethod
    def from_str(s: str):
        if s in "AX":
            return Move.ROCK
        elif s in "BY":
            return Move.PAPER
        elif s in "CZ":
            return Move.SCISSORS

    @staticmethod
    def play(a, b) -> RoundResult:
        """Returns the round result of player A"""

        _THROWS_TO_RESULT = {
            Move.ROCK: {
                Move.ROCK: RoundResult.DRAW,
                Move.PAPER: RoundResult.LOSE,
                Move.SCISSORS: RoundResult.WIN,
            },
            Move.PAPER: {
                Move.ROCK: RoundResult.WIN,
                Move.PAPER: RoundResult.DRAW,
                Move.SCISSORS: RoundResult.LOSE,
            },
            Move.SCISSORS: {
                Move.ROCK: RoundResult.LOSE,
                Move.PAPER: RoundResult.WIN,
                Move.SCISSORS: RoundResult.DRAW,
            },
        }

        return _THROWS_TO_RESULT[a][b]

    @staticmethod
    def get_move(a, target_result: RoundResult):
        """Returns the move required to get the target result"""

        _RESULT_TO_THROWS = {
            Move.ROCK: {
                RoundResult.DRAW: Move.ROCK,
                RoundResult.WIN: Move.PAPER,
                RoundResult.LOSE: Move.SCISSORS,
            },
            Move.PAPER: {
                RoundResult.LOSE: Move.ROCK,
                RoundResult.DRAW: Move.PAPER,
                RoundResult.WIN: Move.SCISSORS,
            },
            Move.SCISSORS: {
                RoundResult.WIN: Move.ROCK,
                RoundResult.LOSE: Move.PAPER,
                RoundResult.DRAW: Move.SCISSORS,
            },
        }

        return _RESULT_TO_THROWS[a][target_result]


with open("input.txt") as f:
    part1_score = 0
    part2_score = 0
    for line in f:
        a, b = line.strip().split()
        opponent_pick, my_pick = (Move.from_str(a), Move.from_str(b))
        desired_result = RoundResult.from_str(b)

        part1_score += my_pick.value + Move.play(my_pick, opponent_pick).value
        part2_score += (
            Move.get_move(opponent_pick, desired_result).value + desired_result.value
        )

    print(f"Part 1: {part1_score}")
    print(f"Part 2: {part2_score}")
