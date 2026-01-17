class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS = len(board)
        COLOUMNS = len(board[0])

        def backtrack(i, r, c):
            if i == len(word):
                return True

            if r < 0 or r >= ROWS or c < 0 or c >= COLOUMNS:
                return False

            if board[r][c] == "*" or board[r][c] != word[i]:
                return False
            
            letter = board[r][c]
            board[r][c] = "*"

            found = backtrack(i+1, r+1, c) or backtrack(i+1, r-1, c) or backtrack(i+1, r, c+1) or backtrack(i+1, r, c-1)

            board[r][c] = letter
            return found

        for r in range(ROWS):
            for c in range(COLOUMNS):
                if backtrack(0, r, c):
                    return True
        return False
