class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])

        # 1. Búsqueda binaria para encontrar la fila
        top, bot = 0, ROWS - 1
        while top <= bot:
            row = (top + bot) // 2
            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                bot = row - 1
            else:
                break

        if not (top <= bot):
            return False

        # 2. Búsqueda binaria dentro de la fila candidata
        row = (top + bot) // 2
        L, R = 0, COLS - 1
        while L <= R:
            mid = (L + R) // 2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] < target:
                L = mid + 1
            else:
                R = mid - 1

        return False