# Consider a rectangular h × w board with all cells initially white. You are to process several queries of the following types:

# "x a b" - color the white cell (a, b) (0-based coordinates, the first one is a row index, and the second one is a column index) black;
# "> a b" - find the leftmost white cell to the right of the white cell (a, b);
# "< a b" - find the rightmost white cell to the left of the white cell (a, b);
# "v a b" - the same, but the search should be done downwards;
# "^ a b" - the same, but the search should be done upwards;
# For each query, except the ones of the first type, find the answer.

# Example

# For h = 3, w = 5, and
# queries = ["v 1 2", "x 2 2", "v 1 2", "> 2 1", "x 2 3", "> 2 1", "< 2 0"],
# the output should be
# solution(h, w, queries) = [[2, 2], [-1, -1], [2, 3], [2, 4], [-1, -1]].


def solution(h, w, queries):
    # h = 3
    # w = 5
    # [
    #     [0,0,0,0,0]
    #     [0,0,0,0,0]
    #     [0,0,0,0,0]
    # ]

    matrix = [[True] * w for i in range(h)]

    result = []
    for query in queries:
        command, sx, sy = query.split(" ")
        x = int(sx)
        y = int(sy)

        found = False
        if command == "x":
            matrix[x][y] = False
            continue
        elif command == ">":
            for i in range(y + 1, w):
                if matrix[x][i]:
                    found = True
                    result.append([x, i])
                    break
        elif command == "<":
            for i in range(y - 1, -1, -1):
                if matrix[x][i]:
                    found = True
                    result.append([x, i])
                    break
        elif command == "v":
            for i in range(x + 1, h):
                if matrix[i][y]:
                    found = True
                    result.append([i, y])
                    break
        elif command == "^":
            for i in range(x - 1, -1, -1):
                if matrix[i][x]:
                    found = True
                    result.append([i, x])
                    break

        if not found:
            result.append([-1, -1])
    return result


# [[2, 2], [-1, -1], [2, 3], [2, 4], [-1, -1]]
solution(3, 5, ["v 1 2", "x 2 2", "v 1 2", "> 2 1", "x 2 3", "> 2 1", "< 2 0"])
