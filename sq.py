# lst2D = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15]]
#
#
# def snake(lst2D):
#     new_lst = [row[::-1] if (i + 1) % 2 == 0 else row for i, row in enumerate(lst2D)]
#     flat_list = [num for row in new_lst for num in row]
#     result = " ".join(map(str, flat_list))
#
#     return result
#
#
# print(snake(lst2D))


N = int(input())

matrix = [[0] * N for _ in range(N)]

row, col = 0, 0
current_number = 1

directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
dir_index = 0

for _ in range(N * N):
    matrix[row][col] = current_number
    current_number += 1

    next_row = row + directions[dir_index][0]
    next_col = col + directions[dir_index][1]

    if 0 <= next_row < N and 0 <= next_col < N and matrix[next_row][next_col] == 0:
        row, col = next_row, next_col
    else:
        dir_index = (dir_index + 1) % 4
        row += directions[dir_index][0]
        col += directions[dir_index][1]

for r in matrix:
    print(*(num for num in r))
