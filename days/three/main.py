def count_mask(input: list[str]) -> list[int]:
    num_bits = len(input[0])
    gamma_count = [0] * num_bits

    for diagnostic in input:
        for index, bit in enumerate(diagnostic):
            gamma_count[index] = gamma_count[index] + (-1 if bit == "0" else 1)

    return gamma_count

def filter_by_index(input: list[str], index: int, fallback: int) -> list[str]:
    mask = count_mask(input)

    filter_bit = 1
    if mask[index] < 0:
        filter_bit = 0
    elif mask[index] > 0:
        filter_bit = 1

    if fallback == 0:
        return [line for line in input if int(line[index]) != filter_bit]

    return [line for line in input if int(line[index]) == filter_bit]

def find_unique_line(input: list[str], fallback: int) -> str:
    num_bits = len(input[0])

    for i in range(num_bits):
        input = filter_by_index(input, i, fallback)

        if len(input) == 1:
            break

    return input[0]

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

    oxygen_count = int(find_unique_line(input, fallback=1), 2)
    print(f"oxygen_count: {oxygen_count}")
    co2_count = int(find_unique_line(input, fallback=0), 2)
    print(f"co2_count: {co2_count}")

    print(f"outcome: {oxygen_count*co2_count}")
