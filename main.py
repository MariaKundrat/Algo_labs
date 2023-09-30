def zigzag_function(matrix, reverse=True):
    if not matrix:
        return []

    m, n = len(matrix), len(matrix[0])
    result = []

    if (reverse is False):
        for diagonal_sum in range(m + n - 1):
            if diagonal_sum % 2 == 0:
                if diagonal_sum < m:
                    row, col = diagonal_sum, 0
                else:
                    row, col = m - 1, diagonal_sum - m + 1

                while row >= 0 and col < n:
                    result.append(matrix[row][col])
                    row -= 1
                    col += 1
            else:
                if diagonal_sum < n:
                    row, col = 0, diagonal_sum
                else:
                    row, col = diagonal_sum - n + 1, n - 1

                while row < m and col >= 0:
                    result.append(matrix[row][col])
                    row += 1
                    col -= 1

        return result
    else:
        for diagonal_sum in range(m + n - 1):
            if diagonal_sum % 2 == 0:
                if diagonal_sum < m:
                    row, col = diagonal_sum, 0
                else:
                    row, col = m - 1, diagonal_sum - m + 1

                while row >= 0 and col < n:
                    result.append(matrix[row][col])
                    row -= 1
                    col += 1
            else:
                if diagonal_sum < n:
                    row, col = 0, diagonal_sum
                else:
                    row, col = diagonal_sum - n + 1, n - 1

                while row < m and col >= 0:
                    result.append(matrix[row][col])
                    row += 1
                    col -= 1
        return result[::-1]


matrix1 = [[1, 2, 6],
           [3, 5, 7],
           [4, 8, 9]]
print(zigzag_function(matrix1))

matrix2 = [[1, 2, 6, 7, 12],
           [3, 5, 8, 11, 13],
           [4, 9, 10, 14, 15]]
print(zigzag_function(matrix2))

matrix3 = [[1, 2, 3, 4],
           [5, 6, 7, 8],
           [9, 10, 11, 12],
           [13, 14, 15, 16],
           [17, 18, 19, 20]]
print(zigzag_function(matrix3))
