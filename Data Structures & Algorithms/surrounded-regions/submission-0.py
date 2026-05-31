class Solution:
    def solve(self, board: List[List[str]]) -> None:
        
        surrounded = [[True]*len(board[0]) for row in board]
        visited = [[False]*len(board[0]) for row in board]

        def find_surrounded(x,y):
            if x < 0 or x >= len(board) or y < 0 or y >= len(board[0]):
                return
            
            if visited[x][y]:
                return

            if board[x][y] == "X":
                return
            
            surrounded[x][y] = False
            visited[x][y] = True

            find_surrounded(x - 1, y)
            find_surrounded(x + 1, y)
            find_surrounded(x, y - 1)
            find_surrounded(x, y + 1)

        for i in range(len(board)):
            surrounded[i][0] = False
            surrounded[i][-1] = False
        
        for i in range(len(board[0])):
            surrounded[0][i] = False
            surrounded[-1][i] = False
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if not surrounded[i][j]:
                    find_surrounded(i, j)
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if surrounded[i][j]:
                    board[i][j] = 'X'

        return