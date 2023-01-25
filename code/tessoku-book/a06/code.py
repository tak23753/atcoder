def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))

    total_list = []

    for a in A:
        if total_list:
            total_list.append(total_list[-1] + a)
        else:
            total_list.append(a)

    for _ in range(Q):
        L, R = map(int, input().split())
        print(total_list[R - 1] - total_list[L - 1])

if __name__ == "__main__":
    main()
