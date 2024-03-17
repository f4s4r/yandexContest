def task1():
    N = int(input())
    max_x, max_y = list(map(int, input().split()))
    min_x = max_x
    min_y = max_y
    for i in range(1, N):
        x, y = input().split()
        x, y = int(x), int(y)
        max_x = x if x > max_x else max_x
        min_x = x if x < min_x else min_x
        max_y = y if y > max_y else max_y
        min_y = y if y < min_y else min_y
    return [min_x, min_y, max_x, max_y]


print(*task1())