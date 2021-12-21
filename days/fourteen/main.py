from collections import Counter, defaultdict
from os import pardir

if __name__ == "__main__":
    input = '''NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C'''

    # Read input
    with open("days/fourteen/input.txt") as input_file:
        input = input_file.read()

    polymer_template, pair_insertion_rule_lines = input.strip().split("\n\n")
    polymer_template = list(polymer_template)

    pair_insertion_rules = {}
    for line in pair_insertion_rule_lines.strip().split("\n"):
        pair, result = line.split(" -> ")
        a,b = list(pair)
        pair_insertion_rules[(a,b)] = result

    element_count = defaultdict(int)
    pairs = defaultdict(int)
    for i in range(0, len(polymer_template)):
            a = polymer_template[i]
            element_count[a] += 1

            if i+1 >= len(polymer_template):
                continue

            b = polymer_template[i + 1]

            pairs[(a, b)] += 1

    for x in range(0, 40):
        new_pairs = defaultdict(int)

        for (a,b), count in pairs.items():
            new_element = pair_insertion_rules[(a,b)]
            element_count[new_element] += count

            new_pairs[(a, new_element)] += count
            new_pairs[(new_element, b)] += count

        pairs = new_pairs

    sorted_values = sorted(element_count.values())
    print(sorted_values)
    print(sorted_values[-1] - sorted_values[0])
