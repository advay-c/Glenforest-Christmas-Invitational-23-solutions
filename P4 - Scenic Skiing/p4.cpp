#include <iostream>
#include <vector>
#include <unordered_map>
#include <algorithm>

using namespace std;

// Function to recursively find the longest path starting from a given node in the graph.
int find_longest_path(unordered_map<int, vector<int>>& graph, int node, vector<bool>& visited, vector<int>& dp) {
    // If the node has already been visited, return its previously computed longest path.
    if (visited[node])
        return dp[node];

    // Mark the node as visited.
    visited[node] = true;
    int max_path = 0;

    // Explore all neighbors of the current node and find the maximum path length starting from each neighbor.
    for (int neighbor : graph[node])
        max_path = max(max_path, find_longest_path(graph, neighbor, visited, dp) + 1);

    // Cache the computed longest path for the current node.
    dp[node] = max_path;
    return max_path;
}

// Function to find the maximum number of slopes that can be traversed.
int max_slopes(int checkpoints, vector<pair<int, int>>& slopes) {
    // Create an adjacency list representation of the graph where each checkpoint is a node and slopes represent directed edges.
    unordered_map<int, vector<int>> graph;
    for (const auto& slope : slopes)
        graph[slope.first].push_back(slope.second);

    // Initialize arrays to keep track of visited nodes and longest paths.
    vector<bool> visited(checkpoints + 1, false);
    vector<int> dp(checkpoints + 1, 0);

    int max_slopes = 0;
    // Iterate over each checkpoint and find the longest path starting from it.
    for (int i = 1; i <= checkpoints; ++i)
        max_slopes = max(max_slopes, find_longest_path(graph, i, visited, dp));

    return max_slopes;
}

int main() {
    int checkpoints, slopes_count;
    cin >> checkpoints >> slopes_count;

    vector<pair<int, int>> slopes(slopes_count);
    for (int i = 0; i < slopes_count; ++i)
        cin >> slopes[i].first >> slopes[i].second;

    // Find and print the maximum number of slopes that can be traversed.
    int result = max_slopes(checkpoints, slopes);
    cout << result << endl;

    return 0;
}
