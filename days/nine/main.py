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

    low_points = 0
    for y, line in data.items():
        for x, point in line.items():
            low_point = True

            for a in range(-1, 2):
                if not low_point:
                    break

                for b in range(-1, 2):
                    if not low_point:
                        break

                    is_diagonal = not (a == 0 or b == 0)
                    is_current_point = a == 0 and b == 0
                    if is_diagonal or is_current_point:
                        continue

                    item = data.get(y + a, {}).get(x + b, None)
                    if item == None:
                        continue

                    if point >= item:
                        low_point = False

            if low_point == True:
                print(f"Low point: {point}")
                low_points += 1 + point

    print(low_points)


