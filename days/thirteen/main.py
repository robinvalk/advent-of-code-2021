from collections import defaultdict

if __name__ == "__main__":
    input = '''6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0

fold along y=7
fold along x=5'''

    # Read input
    with open("days/thirteen/input.txt") as input_file:
        input = input_file.read()

    coord_lines, fold_instruction_lines = input.strip().split("\n\n")

    coords = [tuple(line.strip().split(",")) for line in coord_lines.strip().split("\n")]
    fold_instructions = [tuple(line.strip("fold along ").split("=")) for line in fold_instruction_lines.strip().split("\n")]

    paper = defaultdict(bool)
    for (x,y) in coords:
        paper[(int(x), int(y))] = True

    for fold_instruction in fold_instructions[:1]:
        fold_type, axis = fold_instruction
        axis = int(axis)
        new_paper = paper.copy()

        if fold_type == 'y':
            for (x,y), is_marker in new_paper.items():
                if y <= axis:
                    continue

                del paper[(x,y)]
                paper[(x,2*axis-y)] = True
        else:
            for (x,y), is_marker in new_paper.items():
                if x <= axis:
                    continue

                del paper[(x,y)]
                paper[(2*axis-x,y)] = True

    print(len(list(filter(lambda x: x, paper.values()))))
