from collections import deque


def find_trees(nodes, edges):
    if nodes <= 0:
        return []

    # with only one node, since its in-degrees will be 0, therefore, we need to handle it separately
    if nodes == 1:
        return [0]

    # a. Initialize the graph
    inDegree = {i: 0 for i in range(nodes)}  # count of incoming edges
    graph = {i: [] for i in range(nodes)}  # adjacency list graph

    # b. Build the graph
    for edge in edges:
        n1, n2 = edge[0], edge[1]
        # since this is an undirected graph, therefore, add a link for both the nodes
        graph[n1].append(n2)
        graph[n2].append(n1)
        # increment the in-degrees of both the nodes
        inDegree[n1] += 1
        inDegree[n2] += 1

    # c. Find all leaves i.e., all nodes with 0 in-degrees
    leaves = deque()
    for key in inDegree:
        if inDegree[key] == 1:
            leaves.append(key)

    # d. Remove leaves level by level and subtract each leave's children's in-degrees.
    # Repeat this until we are left with 1 or 2 nodes, which will be our answer.
    # Any node that has already been a leaf cannot be the root of a minimum height tree, because
    # its adjacent non-leaf node will always be a better candidate.
    totalNodes = nodes
    while totalNodes > 2:
        totalNodes -= len(leaves)
        for _ in range(len(leaves)):
            node = leaves.popleft()
            for n in graph[node]:
                inDegree[n] -= 1
                if inDegree[n] == 1:
                    leaves.append(n)

    return list(leaves)


def main():
    print("Roots of MHTs: " +
          str(find_trees(5, [[0, 1], [1, 2], [1, 3], [2, 4]])))
    print("Roots of MHTs: " +
          str(find_trees(4, [[0, 1], [0, 2], [2, 3]])))
    print("Roots of MHTs: " +
          str(find_trees(4, [[1, 2], [1, 3]])))


main()
