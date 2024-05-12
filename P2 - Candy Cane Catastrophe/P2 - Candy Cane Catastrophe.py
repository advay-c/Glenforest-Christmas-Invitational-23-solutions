def min_candy_canes(flavours, counts):
    min_count = min(counts)
    total_candy_canes = sum(counts)
    result = total_candy_canes - min_count + 1
    return result

n = int(input())
counts = list(map(int, input().split()))

result = min_candy_canes(n, counts)
print(result)
