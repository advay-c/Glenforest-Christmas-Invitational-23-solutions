n = int(input())
candy_canes = list(map(int, input().split()))
candy_canes.sort(reverse=True)

total = 0
for i in range(n):
    total += max(candy_canes[i], n)
    n -= 1

print(total)