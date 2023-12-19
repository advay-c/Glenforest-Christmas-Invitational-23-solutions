def max_pull_power(N, M, powers):
    max_power = 0

    for i in range(N - M + 1): 
        team1 = powers[i:i+M]
        for j in range(i + M, N - M + 1): 
            team2 = powers[j:j+M]
            total_power = sum(team1) + sum(team2)
            max_power = max(max_power, total_power)

    return max_power

N, M = map(int, input().split())
powers = list(map(int, input().split()))
result = max_pull_power(N, M, powers)
print(result)
