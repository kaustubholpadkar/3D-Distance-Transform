from collections import deque


MAX_DISTANCE = float("inf")


def get_successors(node, height, width, breadth):

    x, y, z, level = node

    new_level = level + 1

    successors = []

    if x - 1 >= 0:
        successors.append((x - 1, y, z, new_level))

    if x + 1 < height:
        successors.append((x + 1, y, z, new_level))

    if y - 1 >= 0:
        successors.append((x, y - 1, z, new_level))

    if y + 1 < width:
        successors.append((x, y + 1, z, new_level))

    if z - 1 >= 0:
        successors.append((x, y, z - 1, new_level))

    if z + 1 < breadth:
        successors.append((x, y, z + 1, new_level))

    return successors


def apply_3d_distance_transform(cube, height, width, breadth):

    level = 0
    queue = deque([])

    visited = []
    distance_transform = []

    for x in range(len(cube)):

        visited.append([])
        distance_transform.append([])

        for y in range(len(cube[x])):

            visited[x].append([])
            distance_transform[x].append([])

            for z in range(len(cube[x][y])):

                visited[x][y].append(False)
                distance_transform[x][y].append(MAX_DISTANCE)

                if cube[x][y][z] == 1:

                    visited[x][y][z] = True
                    distance_transform[x][y][z] = 0.
                    node = x, y, z, level
                    queue.append(node)

    while len(queue):

        node = queue.popleft()

        for successor in get_successors(node, height, width, breadth):
            x, y, z, level = successor

            if visited[x][y][z] is False:
                queue.append(successor)
                distance_transform[x][y][z] = level
                visited[x][y][z] = True

    return distance_transform
