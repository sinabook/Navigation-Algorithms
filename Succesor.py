def get_successors(matrix, x, y):
    successors = []

    # Check up
    if x - 1 >= 0 and matrix[x-1][y]!='X':
        successors.append(matrix[x - 1][y])

    # Check right
    if y + 1 < len(matrix[0]) and matrix[x][y+1]!="X":
        successors.append(matrix[x][y + 1])

    # Check down
    if x + 1 < len(matrix) and matrix[x+1][y]!="X":
        successors.append(matrix[x + 1][y])

    # Check left
    if y - 1 >= 0 and matrix[x][y-1]!="X":
        successors.append(matrix[x][y - 1])

    return successors

