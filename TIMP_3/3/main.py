class Node:
    def __init__(self, row, col, value):
        self.row = row
        self.col = col
        self.value = value


def convert_to_multisparse(matrix):
    multisparse_list = []
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] != 0:
                node = Node(row, col, matrix[row][col])
                multisparse_list.append(node)
    return multisparse_list


# Example usage
matrix = [
    [0, 0, 0, 0],
    [0, 5, 0, 0],
    [0, 0, 0, 8],
    [0, 0, 0, 0]
]

multisparse = convert_to_multisparse(matrix)
for node in multisparse:
    print(f"Row: {node.row}, Column: {node.col}, Value: {node.value}")
