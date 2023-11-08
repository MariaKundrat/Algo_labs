def min_square_size(N, W, H):
    min_size = H if H > W else W
    max_size = H * N if H > W else W * N
    count = 0

    while min_size <= max_size:
        count += 1
        mid = (min_size + max_size) // 2

        rows = mid // W
        cols = mid // H

        if rows * cols >= N:
            max_size = mid - 1
        else:
            min_size = mid + 1

    print(count)
    return min_size


if __name__ == '__main__':
    N, W, H = 9000, 1_000_000_000, 999999999
    result = min_square_size(N, W, H)
    print(result)
