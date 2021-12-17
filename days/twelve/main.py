from collections import defaultdict

if __name__ == "__main__":
    input = '''dc-end
HN-start
start-kj
dc-start
dc-HN
LN-dc
HN-end
kj-sa
kj-HN
kj-dc'''

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
    def follow_path(current_point, path = [], small_caves_visited = [], joker_used = False):
        if current_point in small_caves_visited and joker_used:
            return

        if current_point in small_caves_visited and not joker_used and current_point not in ['start', 'end']:
            joker_used = True

        if current_point == 'start' and current_point in small_caves_visited:
            return

        path.append(current_point)

        if current_point.islower():
            small_caves_visited.append(current_point)

        if current_point == 'end':
            routes.append(path)
            return

        for option in connections[current_point]:
            follow_path(option, path.copy(), small_caves_visited.copy(), joker_used)

    follow_path('start')

    print(len(routes))


