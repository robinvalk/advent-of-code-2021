from collections import defaultdict
from math import floor

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

    scores = []
    scoring = {'}': 3, ')': 1, '>': 4, ']': 2}
    for y, line in enumerate(lines):
        line_sum = 0
        closing_characters_expected = []

        line_corrupt = False
        for x, character in enumerate(line):
            is_opening_character = character in opening_characters.keys()

            if is_opening_character:
                closing_characters_expected.append(opening_characters[character])
                continue

            expected_closing_character = closing_characters_expected.pop()
            if expected_closing_character != character:
                line_corrupt = True
                break

        if line_corrupt:
            continue

        for closing_character in reversed(closing_characters_expected):
            line_sum = line_sum * 5 + scoring[closing_character]

        scores.append(line_sum)

    scores.sort()

    print(scores)

    print(scores[floor(len(scores) / 2)])
