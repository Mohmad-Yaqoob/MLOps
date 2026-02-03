def magic_square(n):
    if n % 2 == 0:
        raise ValueError("Magic square works for odd n only.")

    square = [[0] * n for _ in range(n)]

    i, j = 0, n // 2

    for num in range(1, n * n + 1):
        square[i][j] = num

        # move up and right
        new_i, new_j = (i - 1) % n, (j + 1) % n

        # if cell already filled, move down instead
        if square[new_i][new_j]:
            i = (i + 1) % n
        else:
            i, j = new_i, new_j

    return square


def print_square(square):
    for row in square:
        print(" ".join(f"{num:2}" for num in row))


n = 5 
ms = magic_square(n)
print_square(ms)
