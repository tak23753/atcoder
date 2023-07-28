N, L = map(int, input().split())
K = int(input())
A = list(map(int, input().split()))

def check(x):
    count = 0
    prev = 0

    for i in range(N):
        if A[i] - prev >= x:
            count += 1
            prev = A[i]

    if L - prev >= x:
        count += 1

    return (count >= K + 1)

left, right = -1, L + 1
while right - left > 1:
    mid = (left + right) // 2

    if check(mid):
        left = mid
    else:
        right = mid

print(left)
