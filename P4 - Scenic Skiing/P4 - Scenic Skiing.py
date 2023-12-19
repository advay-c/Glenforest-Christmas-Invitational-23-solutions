# Rohan Dhanam, Advay Chandorkar, Waleed Altobji

from collections import defaultdict

def find_longest_path(graph, node, visited, dp):
    if visited[node]:
        return dp[node]

    visited[node] = True
    max_path = 0

    for neighbor in graph[node]:
        max_path = max(max_path, find_longest_path(graph, neighbor, visited, dp) + 1)

    dp[node] = max_path
    return max_path

def max_slopes(checkpoints, slopes):
    graph = defaultdict(list)

    for a, b in slopes:
        graph[a].append(b)

    visited = [False] * (checkpoints + 1)
    dp = [0] * (checkpoints + 1)

    max_slopes = 0
    for i in range(1, checkpoints + 1):
        max_slopes = max(max_slopes, find_longest_path(graph, i, visited, dp))

    return max_slopes

checkpoints, slopes_count = map(int, input().split())
slopes = [tuple(map(int, input().split())) for _ in range(slopes_count)]

result = max_slopes(checkpoints, slopes)
print(result)
