if __name__ == "__main__":
    input = [
        "00100",
        "11110",
        "10110",
        "10111",
        "10101",
        "01111",
        "00111",
        "11100",
        "10000",
        "11001",
        "00010",
        "01010",
    ]

    # Read input
    with open("days/three/input.txt") as input_file:
        input = [line.strip() for line in input_file.readlines()]

    num_bits = len(input[0])
    gamma_count = [0] * num_bits

    for diagnostic in input:
        for index, bit in enumerate(diagnostic):
            gamma_count[index] = gamma_count[index] + (-1 if bit == "0" else 1)

    gamma_binary_array = [1 if x > 0 else 0 for x in gamma_count]
    gamma_binary_string = ''.join(str(x) for x in gamma_binary_array)

    gamma_rate = int(gamma_binary_string, 2)
    epsilon_rate = gamma_rate ^ int(''.join(str(x) for x in ([1] * num_bits)), 2)

    print(f"output: {gamma_rate*epsilon_rate}")
