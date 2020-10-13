def find_order(words):
    in_degree = {}
    graph = {}
    for word in words:
        for c in word:
            in_degree[c] = 0
            graph[c] = []

    for i in range(len(words) - 1):
        word1 = words[i]
        word2 = words[i + 1]
        for j in range(min(len(word1), len(word2))):
            w1 = word1[j]
            w2 = word2[j]
            if w1 != w2:
                graph[w1].append(w2)
                in_degree[w2] += 1
                break
    from collections import deque
    queue = deque()
    for k, v in in_degree.items():
        if v == 0:
            queue.append(k)
    res = []
    while queue:
        node = queue.popleft()
        res.append(node)
        for n in graph[node]:
            in_degree[n] -= 1
            if in_degree[n] == 0:
                queue.append(n)

    return ''.join(res)


def main():
    print("Character order: " + find_order(["ba", "bc", "ac", "cab"]))
    print("Character order: " + find_order(["cab", "aaa", "aab"]))
    print("Character order: " + find_order(["ywx", "wz", "xww", "xz", "zyy", "zwz"]))


main()
