#include <iostream>
#include <vector>
#include <algorithm>
#include <numeric> // Include this for the accumulate function

using namespace std;

int max_pull_power(int N, int M, vector<int>& powers) {
    int max_power = 0;

    for (int i = 0; i <= N - M; ++i) {
        vector<int> team1(powers.begin() + i, powers.begin() + i + M);
        for (int j = i + M; j <= N - M; ++j) {
            vector<int> team2(powers.begin() + j, powers.begin() + j + M);
            int total_power = accumulate(team1.begin(), team1.end(), 0) + accumulate(team2.begin(), team2.end(), 0);
            max_power = max(max_power, total_power);
        }
    }

    return max_power;
}

int main() {
    int N, M;
    cin >> N >> M;
    vector<int> powers(N);
    for (int i = 0; i < N; ++i)
        cin >> powers[i];

    int result = max_pull_power(N, M, powers);
    cout << result << endl;

    return 0;
}
