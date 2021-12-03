if __name__ == "__main__":
    input = [
        "forward 5",
        "down 5",
        "forward 8",
        "up 3",
        "down 8",
        "forward 2"
    ]

    # Read input
    with open("days/two/input.txt") as input_file:
        input = [line.strip() for line in input_file.readlines()]

    horizontal = 0
    dept = 0
    aim = 0

    for command in input:
        action, distance = command.split(" ")

        if action == 'forward':
            horizontal += int(distance)
            dept += int(distance) * aim
        elif action == 'down':
            aim += int(distance)
        elif action == 'up':
            aim -= int(distance)

    print(f"Horizontal: {horizontal}, Dept: {dept}")
    print(f"Course: {horizontal*dept}")
