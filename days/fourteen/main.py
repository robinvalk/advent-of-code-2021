from collections import Counter

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

    for x in range(0, 10):
        print(f"Step {x}")
        polymer_template_increment = polymer_template.copy()

        for i in range(0, len(polymer_template) - 1):
            a = polymer_template[i]
            b = polymer_template[i + 1]
            polymer_template_increment.insert(i+1+i, pair_insertion_rules[(a,b)])

        polymer_template = polymer_template_increment


    print("Start counting")
    counter = Counter(polymer_template)
    most = counter.most_common()[0]
    least = counter.most_common()[-1]
    print(f"{most[1]} - {least[1]} = {most[1] - least[1]}")
