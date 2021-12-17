from collections import defaultdict

if __name__ == "__main__":
    input = '''5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526'''

    # Read input
    with open("days/eleven/input.txt") as input_file:
        input = input_file.read()

    flash_count = 0
    flashed = defaultdict(bool)
    lines = [[int(x) for x in list(line.strip())] for line in input.split("\n")]

    def increase_neighbours(y, x, should_increase = False):
        global flash_count

        if y == -1 or y >= len(lines) or x == -1 or x >= len(lines[y]):
            return

        if should_increase:
            lines[y][x] += 1

        if lines[y][x] > 9:
            if not flashed[(y,x)]:
                flashed[(y,x)] = True
                flash_count += 1

                for i in range(-1, 2):
                    for u in range(-1, 2):
                        if i == 0 and u == 0:
                            continue

                        increase_neighbours(y+i, x+u, True)

    for i in range(0, 100000000):
        flash_count = 0
        flashed = defaultdict(bool)

        for y, line in enumerate(lines):
            for x, energy_level in enumerate(line):
                lines[y][x] += 1

        for y, line in enumerate(lines):
            for x, energy_level in enumerate(line):
                increase_neighbours(y, x)

        for y, line in enumerate(lines):
            for x, energy_level in enumerate(line):
                if flashed[(y, x)]:
                    lines[y][x] = 0

        if flash_count == 10*10:
            print(i+1)
            break
