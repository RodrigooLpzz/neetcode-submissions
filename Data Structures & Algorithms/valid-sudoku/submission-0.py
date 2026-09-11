class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = collections.defaultdict(set)


        for row in range(9):
            for column in range(9):
                val = board[row][column]

                if val == ".":
                    continue

                box_key = (row // 3, column // 3)

                if val in boxes[box_key] or val in rows[row] or val in cols[column]:
                    return False

                boxes[box_key].add(val)
                rows[row].add(val)
                cols[column].add(val)

        return True