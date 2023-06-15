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
    rows = collections.defaultdict(list)
    cols = collections.defaultdict(list)
    boxes = collections.defaultdict(list)
    for r in range(9):
        for c in range(9):
            if board[r][c] == ".":
                continue
            if (board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in boxes[((r // 3) * 3 + c // 3)]):
                return False
            rows[r].append(board[r][c])
            cols[c].append(board[r][c])
            boxes[(r // 3) * 3 + c // 3].append(board[r][c])

    print("last row is:", rows)
    print("last column is:", cols)
    print("last box is:", boxes)
    return True

print(isValidSudoku(board))
