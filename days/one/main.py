if __name__ == "__main__":
    report = []

    # Read input
    with open("days/one/input.txt") as input_file:
        report = [int(line.strip()) for line in input_file.readlines()]

    # Count times measurment increased
    increases = 0
    last_measurement = report[0]
    for measurement in report[1:]:
        if last_measurement <= measurement:
            increases+=1

        last_measurement = measurement

    print(increases)
