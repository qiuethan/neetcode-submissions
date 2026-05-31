class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        def search(x, y, remaining_word, visited):
            if len(remaining_word) == 0:
                return True

            if x < 0 or x >= len(board):
                return False
            if y < 0 or y >= len(board[0]):
                return False

            if (x, y) in visited:
                return False

            if board[x][y] != remaining_word[0]:
                return False

            if search(x - 1, y, remaining_word[1:], visited + [(x, y)]):
                return True
            if search(x + 1, y, remaining_word[1:], visited + [(x, y)]):
                return True
            if search(x, y - 1, remaining_word[1:], visited + [(x, y)]):
                return True
            if search(x, y + 1, remaining_word[1:], visited + [(x, y)]):
                return True

            return False
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if search(i, j, word, []):
                    return True
        
        return False


