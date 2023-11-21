def is_solved(board: list[list[int]]):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != 0:
            return board[i][0]
        if board[0][i] == board[i][1] == board[2][i] and board[0][i] != 0:
            return board[0][i]

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != 0:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != 0:
        return board[0][2]

    if all(ceil != 0 for row in board for ceil in row):
        return 0
    return -1


board = [[1, 2, 1], [1, 1, 2], [2, 2, 0]]

print(is_solved(board))


def ips_between(start, end):
    def ip_to_int(ip):
        part = list(map(int, ip.split(".")))
        return part[0] * 256**3 + part[1] * 256**2 + part[2] * 256 + part[3]

    start_int = ip_to_int(start)
    end_int = ip_to_int(end)
    return end_int - start_int


print(ips_between("10.0.0.0", "10.0.1.0"))
