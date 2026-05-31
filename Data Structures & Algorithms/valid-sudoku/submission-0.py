class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [[False]*10 for i in range(9)]
        columns = [[False]*10 for i in range(9)]
        squares = [[[False]*10 for i in range(3)] for j in range(3)]

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] != ".":
                    boardVal = int(board[i][j])
                    if rows[i][boardVal]:
                        return False
                    if columns[j][boardVal]:
                        return False
                    if squares[i//3 - 1][j//3 - 1][boardVal]:
                        return False
                    
                    rows[i][boardVal] = True
                    columns[j][boardVal] = True
                    squares[i//3 - 1][j//3 - 1][boardVal] = True
        
        return True