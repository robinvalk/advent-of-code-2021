from collections import defaultdict

if __name__ == "__main__":
    input = '''[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]'''

    # Read input
    with open("days/ten/input.txt") as input_file:
        input = input_file.read()

    opening_characters = {'{': '}', '[': ']', '(': ')', '<': '>'}
    lines = [list(line.strip()) for line in input.split("\n")]
    failing_characters = defaultdict(int)

    for y, line in enumerate(lines):
        closing_characters_expected = []

        for x, character in enumerate(line):
            is_opening_character = character in opening_characters.keys()

            if is_opening_character:
                closing_characters_expected.append(opening_characters[character])
                continue

            expected_closing_character = closing_characters_expected.pop()
            if expected_closing_character != character:
                failing_characters[character] += 1
                break

    sum = 0
    scoring = {'}': 1197, ')': 3, '>': 25137, ']': 57}
    for character, count in failing_characters.items():
        sum += count * scoring[character]

    print(sum)
