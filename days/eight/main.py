
from os import X_OK


if __name__ == "__main__":
    input = '''be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce'''

    # Read input
    # with open("days/eight/input.txt") as input_file:
    #     input = input_file.read()

    count = 0
    unique_digit_numbers = [2, 4, 3, 7]

    results = []

    for line in input.strip().split("\n"):
        digits = {}
        segments = {}
        signal_pattern, output_value = line.strip().split(" | ")

        digit_mapping = {}
        signals = signal_pattern.strip().split(" ")
        signals_to_process = signals
        while len(digit_mapping) < 10:
            for signal in signals_to_process:
                signal_segments = ''.join(sorted(list(signal)))

                if len(signal_segments) == 2:
                    digit_mapping[1] = signal_segments
                if len(signal_segments) == 4:
                    digit_mapping[4] = signal_segments
                if len(signal_segments) == 3:
                    digit_mapping[7] = signal_segments
                if len(signal_segments) == 7:
                    digit_mapping[8] = signal_segments
                if len(signal_segments) == 5 and digit_mapping.get(1) != None:
                    if len(set(signal_segments).intersection(set(digit_mapping.get(1, ())))) == 2:
                        digit_mapping[3] = signal_segments
                    elif len(set(signal_segments).intersection(set(digit_mapping.get(6, ())))) == 5:
                        digit_mapping[5] = signal_segments
                    else:
                        digit_mapping[2] = signal_segments
                if len(signal_segments) == 6:
                    if len(set(signal_segments).intersection(set(digit_mapping.get(4, ())))) == 4:
                        digit_mapping[9] = signal_segments
                    elif len(set(signal_segments).intersection(set(digit_mapping.get(1, ())))) == 2:
                        digit_mapping[0] = signal_segments
                    else:
                        digit_mapping[6] = signal_segments


        number = ''
        for output_number in [''.join(sorted(x)) for x in output_value.strip().split(" ")]:
            key, value = list(filter(lambda x: x[1] == output_number, digit_mapping.items()))[0]
            number += str(key)

        results.append(int(number))

    print(sum(results))
