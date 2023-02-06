def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())

    total_list = []
    for a in A:
        if total_list:
            total_list.append(total_list[-1] + a)
        else:
            total_list.append(a)

    for _ in range(Q):
        L, R = map(int, input().split())

        x = total_list[R - 1] - total_list[L - 2]
        y = (R - L + 1) / 2

        if x > y:
            ans = "win"
        elif x == y:
            ans = "draw"
        else:
            ans = "lose"

        print(ans)

if __name__ == "__main__":
    main()
