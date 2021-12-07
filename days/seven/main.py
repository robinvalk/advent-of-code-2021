def calc_fuel_usage(current_pos, next_pos):
    base = abs(current_pos - next_pos)

    result = 0
    for count in range(base, 0, -1):
        result += count

    return result


if __name__ == "__main__":
    input = "16,1,2,0,4,2,7,1,2,14"

    # Read input
    with open("days/seven/input.txt") as input_file:
        input = input_file.read()

    positions = [int(x) for x in input.strip().split(",")]
    max_pos = max(positions)

    all_diffs = {}
    for pos in range(max_pos):
        diffs = map(lambda x: calc_fuel_usage(x, pos), positions)
        all_diffs[pos] = sum(diffs)

    print(min(all_diffs.values()))
