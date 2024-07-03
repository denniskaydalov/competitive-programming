for _ in range(int(input())):
    # n = int(input)
    n, k = list(map(int, input().split()))
    # a = list(map(int, input().split()))
    # s = input()

    print(k * (n - 1) + 1)
