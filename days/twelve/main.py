from collections import defaultdict

if __name__ == "__main__":
    input = '''start-A
start-b
A-c
A-b
b-d
A-end
b-end'''

    # Read input
    with open("days/twelve/input.txt") as input_file:
        input = input_file.read()

    print(input)

    lines = [tuple(line.strip().split("-")) for line in input.strip().split("\n")]

    connections = defaultdict(list)
    for (a, b) in lines:
        connections[a].append(b)
        connections[b].append(a)

    routes = []
    def follow_path(current_point, path = [], small_caves_visited = []):
        if current_point in small_caves_visited:
            return

        path.append(current_point)

        if current_point.islower():
            small_caves_visited.append(current_point)

        if current_point == 'end':
            routes.append(path)
            return

        for option in connections[current_point]:
            follow_path(option, path.copy(), small_caves_visited.copy())


    follow_path('start')

    print(len(routes))


