def solution(board, moves):
    arr = []
    check = 0
    board_check = {}
    for i,j in enumerate(board):
        board_check[i] = j
    for i in moves:
        for k in board_check:
            if board_check[k][i-1] != 0:
                arr.append(board_check[k][i-1])
                board_check[k][i - 1] = 0
                if len(arr) > 1:
                    if arr[-1] == arr[-2]:
                        arr.pop(-1)
                        arr.pop(-1)
                        check += 2
                break
    return check