board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]
board_check = {}
arr = []
for i,j in enumerate(board):
    board_check[i] = j
for i in moves:
    for k in board_check:
        if board_check[k][i-1] != 0:
            arr.append(board_check[k][i-1])
            board_check[k][i - 1] = 0

            break

print(arr)