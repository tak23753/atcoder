def main():
    N, K = map(int, input().split())

    S = []
    for _ in range(N):
        S.append(input())

    S = S[0:K]

    S.sort()

    for k in range(K):
        print(S[k])

if __name__ == "__main__":
    main()
