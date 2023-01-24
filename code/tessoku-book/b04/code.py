N = input()

a = 1
ans = 0

for n in reversed(N):
    ans += int(n) * a

    a = a * 2

print(ans)
