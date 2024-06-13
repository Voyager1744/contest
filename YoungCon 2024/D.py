def main():
    import sys
    input = sys.stdin.read
    from collections import defaultdict, deque

    n = int(input().strip())
    relationships = [input().strip() for _ in range(n)]

    graph = defaultdict(list)
    indegree = [0] * (n + 1)  # indegree for 1-based indexing

    for i in range(n):
        for j in range(n):
            relation = relationships[i][j]
            if relation == '=':
                graph[i + 1].append(j + 1)
                graph[j + 1].append(i + 1)
            elif relation == '<':
                graph[i + 1].append(j + 1)
                indegree[j + 1] += 1
            elif relation == '>':
                graph[j + 1].append(i + 1)
                indegree[i + 1] += 1
            elif relation == '!':
                # i is not subset of j
                pass
            elif relation == '^':
                # j is not subset of i
                pass

    # Kahn's algorithm for topological sorting
    topo_order = []
    zero_indegree_queue = deque()

    for node in range(1, n + 1):
        if indegree[node] == 0:
            zero_indegree_queue.append(node)

    while zero_indegree_queue:
        current = zero_indegree_queue.popleft()
        topo_order.append(current)
        for neighbor in graph[current]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                zero_indegree_queue.append(neighbor)

    if len(topo_order) != n:
        print("No")
    else:
        print("Yes")
        for node in topo_order:
            print(f"{len(graph[node])} " + " ".join(map(str, sorted(graph[node]))))


if __name__ == "__main__":
    main()
