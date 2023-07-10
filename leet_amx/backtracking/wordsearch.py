class Solution:
    def exist(self, board, word: str):
        ROWS , COLS = len(board),len(board[0])
        path = set()

        def dfs(r,c,i):
            if i == len(word):
                return True
            if (r < 0 or c < 0) or (r >=ROWS or c >=COLS) or (word[i] != board[r][c]) or ((r,c) in path):
                return False
            path.add((r,c))
            state = (dfs(r-1,c,i+1) or dfs(r+1,c,i+1) or dfs(r,c-1,i+1) or dfs(r,c+1,i+1))
            return state
        for r in range(ROWS):
            for c in range(COLS):
                res = dfs(r,c,0)
                if res:
                    return True
        return False

sol = Solution()
board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCCED"
print(sol.exist(board,word))