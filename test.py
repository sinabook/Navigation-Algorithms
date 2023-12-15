def get_successors(matrix, x, y):
    successors = []

    # Check up
    if x - 1 >= 0:
        successors.append(matrix[x - 1][y])

    # Check right
    if y + 1 < len(matrix[0]):
        successors.append(matrix[x][y + 1])

    # Check down
    if x + 1 < len(matrix):
        successors.append(matrix[x + 1][y])

    # Check left
    if y - 1 >= 0:
        successors.append(matrix[x][y - 1])

    return successors

# Example usage
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

y = 2  # Example x coordinate
x = 1  # Example y coordinate

successors = get_successors(matrix, x, y)

print(f"Successors of element at position ({x}, {y}): {successors}")