if __name__ == "__main__":
    input = "3,4,3,1,2"

    # Read input
    with open("days/six/input.txt") as input_file:
        input = input_file.read()

    num_days = 256
    counts = [int(x) for x in input.strip().split(",")]
    school = {}

    for fish in counts:
        if school.get(fish) == None:
            school[fish] = 1
        else:
            school[fish] = 1 + school.get(fish)

    last_run = school
    for i in range(num_days):
        new_run = {}

        for days, num in last_run.items():
            if days != 0:
                new_run[days - 1] = new_run.get(days - 1, 0) + last_run.get(days, 0)
            else:
                new_run[6] = new_run.get(6, 0) + num
                new_run[8] = num

        last_run = new_run

    print(sum(last_run.values()))
