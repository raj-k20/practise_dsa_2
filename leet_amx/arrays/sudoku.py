class Solution:
    def isValidSudoku(self, board) -> bool:
        rows = {}
        columns = {}
        squares = {}
        for r in range(9):
            rows[r] = rows.setdefault(r, [])
            for c in range(9):
                columns[c] = columns.setdefault(c, [])
                if board[r][c] == ".":
                    continue
                if (
                        board[r][c] in rows[r]
                        or board[r][c] in columns[c]
                        or board[r][c] in squares.setdefault((r // 3, c // 3), [])
                ):
                    return False
                columns[c].append(board[r][c])
                rows[r].append(board[r][c])
                squares[(r // 3, c // 3)].append(board[r][c])
        return True


board = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

sol = Solution()
print(sol.isValidSudoku(board))


