from collections import defaultdict

if __name__ == "__main__":
    input = '''2199943210
            3987894921
            9856789892
            8767896789
            9899965678'''

    # Read input
    with open("days/nine/input.txt") as input_file:
        input = input_file.read()

    lines = [list(line.strip()) for line in input.split("\n")]
    data = {index: {i: int(v) for i, v in enumerate(x)} for index, x in enumerate(lines)}
    visited = defaultdict(dict)

    def check_point(y, x, basin_count):
        is_visited = visited[y].get(x, False)
        point_data = data.get(y, {}).get(x, 10)

        if is_visited or point_data >= 9:
            visited[y][x] = True
            return basin_count

        visited[y][x] = True

        basin_count = check_point(y-1, x, basin_count)
        basin_count = check_point(y+1, x, basin_count)
        basin_count = check_point(y, x-1, basin_count)
        basin_count = check_point(y, x+1, basin_count)

        return basin_count + 1

    basins = []
    for y, line in data.items():
        for x, point in line.items():
            if visited[y].get(x, False):
                continue

            if point >= 9:
                visited[y][x] = True
                continue

            basins.append(
                check_point(y, x, 0)
            )

    basins.sort(reverse=True)

    sum = 1
    for x in basins[:3]:
        sum *= x

    print(sum)
