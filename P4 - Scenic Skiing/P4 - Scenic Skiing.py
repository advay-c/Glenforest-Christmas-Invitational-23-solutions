# dp solution
from collections import defaultdict

# This function recursively finds the longest path starting from a given node
# in the graph.
def find_longest_path(graph, node, visited, dp):
    # If the node has already been visited, return its previously computed
    # longest path.
    if visited[node]:
        return dp[node]

    # Mark the node as visited.
    visited[node] = True
    max_path = 0

    # Explore all neighbors of the current node and find the maximum path
    # length starting from each neighbor.
    for neighbor in graph[node]:
        max_path = max(max_path, find_longest_path(graph, neighbor, visited, dp) + 1)

    # Cache the computed longest path for the current node.
    dp[node] = max_path
    return max_path

# This function finds the maximum number of slopes that can be traversed.
def max_slopes(checkpoints, slopes):
    # Create an adjacency list representation of the graph where each checkpoint
    # is a node and slopes represent directed edges.
    graph = defaultdict(list)
    for a, b in slopes:
        graph[a].append(b)

    # Initialize arrays to keep track of visited nodes and longest paths.
    visited = [False] * (checkpoints + 1)
    dp = [0] * (checkpoints + 1)

    max_slopes = 0
    # Iterate over each checkpoint and find the longest path starting from it.
    for i in range(1, checkpoints + 1):
        max_slopes = max(max_slopes, find_longest_path(graph, i, visited, dp))

    return max_slopes

# Read input: number of checkpoints and number of slopes
checkpoints, slopes_count = map(int, input().split())
# Read input: slopes as pairs of integers
slopes = [tuple(map(int, input().split())) for _ in range(slopes_count)]

# Find and print the maximum number of slopes that can be traversed.
result = max_slopes(checkpoints, slopes)
print(result)
