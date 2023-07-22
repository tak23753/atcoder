def main():
    D = int(input())
    N = int(input())
    L = []
    R = []
    x = [0] * D

    for _ in range(N):
        l, r = map(int, input().split())
        L.append(l)
        R.append(r)j 

    for n in range(N):
        x[L[n] - 1] += 1
        x[R[n] - 1] -= 1

    ans = []
    for d in range(D):
        if ans:
            ans.append(ans[-1] + x[d])
        else:
            ans.append(x[d])

    for a in ans:
        print(a)

if __name__ == "__main__":
    main()
