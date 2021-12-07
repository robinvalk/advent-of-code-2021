if __name__ == "__main__":
    input = "3,4,3,1,2"

    # Read input
    with open("days/six/input.txt") as input_file:
        input = input_file.read()

    num_days = 80
    school = [int(x) for x in input.strip().split(",")]

    for i in range(num_days):
        for fishIndex, daysLeft in enumerate(school):
            if daysLeft == 0:
                school[fishIndex] = 7
                school.insert(0, 8)
            else:
                school[fishIndex] = school[fishIndex] - 1

    print(len(school))
