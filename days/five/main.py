from __future__ import annotations
from dataclasses import dataclass

@dataclass
class Line:
    start_coord: tuple[int, int]
    end_coord: tuple[int, int]

    def isStraightLine(self) -> bool:
        return self.start_coord[0] == self.end_coord[0] or self.start_coord[1] == self.end_coord[1]

    def fill(self, count_map: map[str, int]) -> bool:
        start_x, end_x = sorted([self.start_coord[0], self.end_coord[0]])
        start_y, end_y = sorted([self.start_coord[1], self.end_coord[1]])

        if self.isStraightLine():
            x_range = range(start_x, end_x+1)
            y_range = range(start_y, end_y+1)

            for x in x_range:
                for y in y_range:
                    key = f"{x}:{y}"
                    if count_map.get(key) is None:
                        count_map[key] = 1
                    else:
                        count_map[key] = count_map[key] + 1
        else:
            x_index = self.start_coord[0]
            y_index = self.start_coord[1]

            if self.start_coord[0] <= self.end_coord[0]:
                while x_index <= self.end_coord[0]:
                    key = f"{x_index}:{y_index}"
                    if count_map.get(key) is None:
                        count_map[key] = 1
                    else:
                        count_map[key] = count_map[key] + 1

                    x_index = x_index+1
                    if self.start_coord[1] <= self.end_coord[1]:
                        y_index = y_index+1
                    else:
                        y_index = y_index-1
            else:
                while x_index >= self.end_coord[0]:
                    key = f"{x_index}:{y_index}"
                    if count_map.get(key) is None:
                        count_map[key] = 1
                    else:
                        count_map[key] = count_map[key] + 1

                    x_index = x_index-1
                    if self.start_coord[1] <= self.end_coord[1]:
                        y_index = y_index+1
                    else:
                        y_index = y_index-1

        return count_map

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

    count_map = {}
    for line in lines:
        count_map = line.fill(count_map)

    filtered_count = len(list(filter(lambda x: x >= 2, count_map.values())))
    print(filtered_count)
