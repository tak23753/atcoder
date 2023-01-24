N = int(input())
A = list(map(int, input().split()))

ans = 'No'

for i, a1 in enumerate(A):
    for j, a2 in enumerate(A):
        if i == j:
            continue
        for k, a3 in enumerate(A):
            if i == k or k == j:
                continue
            
            if a1 + a2 + a3 == 1000:
                ans = 'Yes'

print(ans)
