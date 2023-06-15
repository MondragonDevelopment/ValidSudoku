import collections

board = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

def isValidSudoku(board):
    b = [[]] * 9
    for i in range(9):
        r = []
        c = []
        for j in range(9):

            if board[i][j] != "." and board[i][j] in r:
                return False
            r.append(board[i][j])
            if board[j][i] != "." and board[j][i] in c:
                return False
            c.append(board[j][i])
            # if board[i][j] != "." and board[i][j] in b[((i//3) * 3 + j//3)]:
            #     return False
            b[((i//3) * 3 + j//3)].append(board[i][j])


    print("last row is:", r)
    print("last column is:", c)
    print("last box is:", b)
    return True

print(isValidSudoku(board))
