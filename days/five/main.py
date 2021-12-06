from __future__ import annotations
from dataclasses import dataclass

@dataclass
class Line:
    start_coord: tuple[int, int]
    end_coord: tuple[int, int]

    def getMaxX(self) -> int:
        return self.start_coord[0] if self.start_coord[0] >= self.end_coord[0] else self.end_coord[0]
    def getMaxY(self) -> int:
        return self.start_coord[1] if self.start_coord[1] >= self.end_coord[1] else self.end_coord[1]

    def isInStraightLine(self) -> bool:
        return self.start_coord[0] == self.end_coord[0] or self.start_coord[1] == self.end_coord[1]

    def isXBetween(self, x: int) -> bool:
        start = self.start_coord[0]
        end = self.end_coord[0]

        if start <= end:
            return start <= x and end >= x
        else:
            return end <= x and start >= x

    def isYBetween(self, y: int) -> bool:
        start = self.start_coord[1]
        end = self.end_coord[1]

        if start <= end:
            return start <= y and end >= y
        else:
            return end <= y and start >= y

def matrix_gen(rows: int, cols: int) -> list[list[bool]]:
    return [[False for x in range(cols)] for x in range(rows)]

def parse_input(input: str) -> list[Line]:
    lines = []

    for line in input.strip().split("\n"):
        start, end = line.strip().split(" -> ")
        start_x, start_y = start.strip().split(",")
        end_x, end_y = end.split(",")

        lines.append(Line((int(start_x), int(start_y)), (int(end_x), int(end_y))))

    return lines

if __name__ == "__main__":
    input = '''
0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2
    '''

    # Read input
    with open("days/five/input.txt") as input_file:
        input = input_file.read()

    lines = parse_input(input)
    highest_x_line = sorted(lines, key=lambda x: x.getMaxX(), reverse=True)[0]
    highest_y_line = sorted(lines, key=lambda x: x.getMaxY(), reverse=True)[0]

    count_map = {}
    filtered_lines = list(filter(lambda x: x.isInStraightLine(), lines))

    for x in range(highest_x_line.getMaxX() + 1):
        for y in range(highest_y_line.getMaxY() + 1):
            for line in filtered_lines:
                if line.isXBetween(x) and line.isYBetween(y):
                    key = f"{x}:{y}"
                    if count_map.get(key) is None:
                        count_map[key] = 1
                    else:
                        count_map[key] = count_map[key] + 1


    filtered_count = len(list(filter(lambda x: x >= 2, count_map.values())))
    print(filtered_count)
