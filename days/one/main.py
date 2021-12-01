if __name__ == "__main__":
    report = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]

    # Read input
    with open("days/one/input.txt") as input_file:
        report = [int(line.strip()) for line in input_file.readlines()]

    # Count times measurment increased
    increases = 0
    last_measurement = None
    for index, mes in enumerate(report):
        if last_measurement is None:
            last_measurement = sum(report[:3])
            continue

        window = report[index:(index+3)]
        if len(window) < 3:
            break

        new_sum = sum(window)
        if new_sum > last_measurement:
            increases+=1

        last_measurement = new_sum

    print(increases)
