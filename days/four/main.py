from __future__ import annotations
from dataclasses import dataclass


@dataclass
class Card:
    numbers: list[list[int]]
    marked: list[list[bool]]

    def mark(self, number: int) -> Card:
        for rowIndex, row in enumerate(self.numbers):
            for colIndex, x in enumerate(row):
                if x == number:
                    self.marked[rowIndex][colIndex] = True
                    break

        return self

    def hasBingo(self) -> bool:
        # Check row bingo
        for row in self.marked:
            if len([x for x in row if x == False]) == 0:
                return True

        # Check col bingo
        for colIndex, _ in enumerate(self.marked[0]):
            col_has_false = False

            for rowIndex, row in enumerate(self.marked):
                if self.marked[rowIndex][colIndex] == False:
                    col_has_false = True
                    break

            if not col_has_false:
                return True

    def sumUnmarked(self) -> int:
        sum_unmarked = 0
        for rowId, row in enumerate(self.marked):
            for colId, mark in enumerate(row):
                if mark == False:
                    sum_unmarked = sum_unmarked + self.numbers[rowId][colId]

        return sum_unmarked

def matrix_gen(rows: int, cols: int) -> list[list[bool]]:
    return [[False for x in range(cols)] for x in range(rows)]

def parse_input(input: str) -> tuple[list[int], list[list[int]]]:
    numbers_string, *boards_string_array = input.split("\n\n")
    numbers_array = [int(x) for x in numbers_string.strip().split(",")]

    boards = []
    for board_string in boards_string_array:
        board = []
        for board_line in board_string.strip().split("\n"):
            board.append([int(x.strip()) for x in board_line.strip().split(" ") if len(x.strip()) > 0])

        boards.append(
            Card(board, matrix_gen(len(board), len(board[0])))
        )

    return numbers_array, boards

if __name__ == "__main__":
    input = '''
7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7
    '''

    # Read input
    with open("days/four/input.txt") as input_file:
        input = input_file.read()

    numbers, boards = parse_input(input)

    last_won_boards = []
    for number in numbers:
        boards = [board.mark(number) for board in boards]
        bingo_boards = [boardIndex for boardIndex, x in enumerate(boards) if x.hasBingo()]

        if len(bingo_boards) == len(boards):
            last_boards = [x for x in bingo_boards if x not in last_won_boards]
            last_board_index = last_boards[0]

            print(boards[last_board_index].sumUnmarked() * number)
            break
        else:
            last_won_boards = bingo_boards
