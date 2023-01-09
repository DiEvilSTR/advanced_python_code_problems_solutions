from itertools import permutations


def bellman_ford_algorithm(graph):
    rows = len(graph)
    distances = []

    for vertex in range(rows):
        distance = [float("Inf")] * rows
        distance[vertex] = 0

        for a in range(rows):
            for b in range(rows):
                for c in range(rows):
                    cost = graph[b][c]
                    if distance[b] != float("Inf") and distance[b] + cost < distance[c]:
                        distance[c] = distance[b] + cost
        distances.append(distance)

    return distances


def check_for_infinite_cycle(graph):
    # Using Bellman Ford algorithm to check times for infinite loop
    distance = graph[0]
    rows = len(graph)

    for b in range(rows):
        for c in range(rows):
            cost = graph[b][c]
            if distance[b] + cost < distance[c]:
                return True

    return False


def check_time(path_list, graph):
    time = 0
    path = [0] + list(path_list) + [len(graph) - 1]

    for i in range(1, len(path)):
        time += graph[path[i - 1]][path[i]]

    return time


def solution(times, times_limit):
    amount_of_bunnies = len(times) - 2
    bunnies = [x for x in range(1, amount_of_bunnies + 1)]

    distances = bellman_ford_algorithm(times)

    if check_for_infinite_cycle(distances):
        return range(amount_of_bunnies)

    # Creating all possible combinations of saved bunnies and checking if timer allows that
    for bunnies_set in range(amount_of_bunnies, 0, -1):

        for path in permutations(bunnies, bunnies_set):
            time = check_time(path, distances)
            if time <= times_limit:
                return [x - 1 for x in sorted(path)]

    return []

# print(solution([[0, 2, 2, 2, -1], [9, 0, 2, 2, -1], [9, 3, 0, 2, -1], [9, 3, 2, 0, -1], [9, 3, 2, 2, 0]], 1))
# print(solution([[0, 1, 1, 1, 1], [1, 0, 1, 1, 1], [1, 1, 0, 1, 1], [1, 1, 1, 0, 1], [1, 1, 1, 1, 0]], 3))