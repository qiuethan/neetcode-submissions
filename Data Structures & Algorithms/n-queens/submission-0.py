class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        def check_pos(grid, x, y):
            for i in range(n):
                if grid[x][i] == 1: return False
                if grid[i][y] == 1: return False
            
            # diag checks
            i = 1
            while x+i < n and y+i < n:
                if grid[x+i][y+i] == 1: return False
                i += 1
            
            i = 1
            while x-i >= 0 and y-i >= 0:
                if grid[x-i][y-i] == 1: return False
                i += 1

            i = 1
            while x-i >= 0 and y+i < n:
                if grid[x-i][y+i] == 1: return False
                i += 1

            i = 1
            while x+i < n and y-i >= 0:
                if grid[x+i][y-i] == 1: return False
                i += 1

            return True

        sols = []
        grid = [[0]*n for _ in range(n)]

        def make_solution(grid):
            return [
                "".join("Q" if grid[r][c] == 1 else "." for c in range(n))
                for r in range(n)
            ]

        def back_track(queens, row):
            if queens == n:
                sols.append(make_solution(grid))
                return

            if row == n:
                return

            for col in range(n):
                if check_pos(grid, row, col):
                    grid[row][col] = 1
                    back_track(queens + 1, row + 1)
                    grid[row][col] = 0

        back_track(0, 0)
        return sols
