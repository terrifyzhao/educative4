from collections import deque


def can_construct(originalSeq, sequences):
    sortedOrder = []
    if len(originalSeq) <= 0:
        return False

    # a. Initialize the graph
    inDegree = {}  # count of incoming edges
    graph = {}  # adjacency list graph
    for sequence in sequences:
        for num in sequence:
            inDegree[num] = 0
            graph[num] = []

    # b. Build the graph
    for sequence in sequences:
        for i in range(1, len(sequence)):
            parent, child = sequence[i - 1], sequence[i]
            graph[parent].append(child)
            inDegree[child] += 1

    # if we don't have ordering rules for all the numbers we'll not able to uniquely construct the sequence
    if len(inDegree) != len(originalSeq):
        return False

    # c. Find all sources i.e., all vertices with 0 in-degrees
    sources = deque()
    for key in inDegree:
        if inDegree[key] == 0:
            sources.append(key)

    while sources:
        if len(sources) > 1:
            return False

        if originalSeq[len(sortedOrder)] != sources[0]:
            return False

        node = sources.popleft()
        sortedOrder.append(node)
        for n in graph[node]:
            inDegree[n] -= 1
            if inDegree[n] == 0:
                sources.append(n)

    if len(sortedOrder) == len(originalSeq):
        return True
    else:
        return False


def main():
    print("Can construct: " +
          str(can_construct([1, 2, 3, 4], [[1, 2], [2, 3], [3, 4]])))
    print("Can construct: " +
          str(can_construct([1, 2, 3, 4], [[1, 2], [2, 3], [2, 4]])))
    print("Can construct: " +
          str(can_construct([3, 1, 4, 2, 5], [[3, 1, 5], [1, 4, 2, 5]])))


main()
