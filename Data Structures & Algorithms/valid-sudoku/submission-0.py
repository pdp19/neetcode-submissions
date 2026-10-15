class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = [set() for _ in range(9)]
        col = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                value = board[r][c]
                if value == ".":
                    continue
                box = (r//3) * 3 + (c//3)
                if value in row[r]:
                    return False
                if value in col[c]:
                    return False
                if value in boxes[box]:
                    return False
                row[r].add(value)
                col[c].add(value)
                boxes[box].add(value)
        return True
        