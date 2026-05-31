class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        first_col = [row[0] for row in matrix]
        last_col = [row[-1] for row in matrix]

        def find_row(first_col, last_col, target):

            left = 0
            right = len(first_col) - 1

            while left <= right:
                mid = (left + right) // 2
                if first_col[mid] <= target and target <= last_col[mid]:
                    return mid
                elif last_col[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            
            return -1
        
        row = find_row(first_col, last_col, target)

        if row == -1:
            return False

        left = 0
        right = len(matrix[row]) - 1

        while left <= right:
            mid = (left + right) // 2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return False