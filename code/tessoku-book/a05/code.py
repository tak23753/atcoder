N, K = map(int, input().split())

ans = 0

for red in range(1, N + 1):
    for blue in range(1, N + 1):
        if 1 <= K - red - blue <= N:
            ans += 1

print(ans)
