def find_biggest_flow(entrance, exit, path):
    # Adapted Dijkstras Algorithm for Adjacency Matrix
    # Returns a tuple with maximum available bunny flow
    # (max distance) for entrance and exit route for this flow
    n = len(path)

    corridors_size = [-1]*n
    corridors_size[entrance] = path[entrance][entrance]  # 0

    visited_rooms = [False]*n
    previous_rooms = [-1]*n

    bunny_routes = [{}]*n

    # Searching for maximum corridor size sum for every room and mapping previous rooms for all rooms
    for count in range(n-1):
        max_corridors_size = -1
        a = 0

        for b in range(len(visited_rooms)):
            if visited_rooms[b] is False and corridors_size[b] > max_corridors_size:
                max_corridors_size = corridors_size[b]
                a = b

        visited_rooms[a] = True
        for b in range(n):
            if not(visited_rooms[b]) and path[a][b] != 0 and corridors_size[a] + path[a][b] > corridors_size[b]:
                previous_rooms[b] = a
                corridors_size[b] = corridors_size[a] + path[a][b]

    # Building routes with the biggest corridor sums to every room from entrance
    for i in range(n):
        j = i
        s = []
        while previous_rooms[j] != -1:
            s.append(j)
            j = previous_rooms[j]
        s.append(entrance)
        bunny_routes[i] = s[::-1]
    
    # Calculating max available flow as a minimum corridor's size in the route
    max_path_flow = 0
    
    if bunny_routes[exit] != [0]:
        path_flow = []
        for m in range(len(bunny_routes[exit]) - 1):
            path_flow.append(path[bunny_routes[exit][m]][bunny_routes[exit][m + 1]])
        max_path_flow = min(path_flow) if path_flow != [] else 0
    
    return (max_path_flow, bunny_routes[exit])


def solution(entrances, exits, path):
    available_paths = path
    result = 0
    
    for entrance in entrances:

        for exit in exits:
            # Calculating biggest flow available, excluding it and repeating this process while it possible
            biggest_flow = find_biggest_flow(entrance, exit, available_paths)

            while biggest_flow[0] > 0:
                result += biggest_flow[0]

                for m in range(len(biggest_flow[1]) - 1):
                    available_paths[biggest_flow[1][m]][biggest_flow[1][m + 1]] -= biggest_flow[0]
                
                biggest_flow = find_biggest_flow(entrance, exit, available_paths)

    return result


# solution([0], [3], [[0, 7, 0, 0], [0, 0, 6, 0], [0, 0, 0, 8], [9, 0, 0, 0]])
# solution([0, 1], [4, 5], [[0, 0, 4, 6, 0, 0], [0, 0, 5, 2, 0, 0], [0, 0, 0, 0, 4, 4], [0, 0, 0, 0, 6, 6], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]])