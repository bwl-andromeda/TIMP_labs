def count_edges(adj_list, a, b):
    count = 0
    for c in adj_list[a]:
        if c in adj_list[b]:
            count += 1
    return count

def visualize_matrix(adj_list):
    vertices = sorted(adj_list.keys())
    matrix = [[0] * len(vertices) for _ in range(len(vertices))]

    for i in vertices:
        for j in adj_list[i]:
            matrix[i][j] = 1

    return matrix

adj_list = {0: [1, 3], 1: [2], 2: [3], 3: [3, 1]}
for vertex, neighbors in adj_list.items():
    print(f"{vertex}: {neighbors}")

a = 0
b = 2
result = count_edges(adj_list, a, b)
print(f"\nКоличество ребер между вершинами {a} и {b}: {result}")

# Visualize the matrix
matrix = visualize_matrix(adj_list)
for row in matrix:
    print(" ".join(map(str, row)))
