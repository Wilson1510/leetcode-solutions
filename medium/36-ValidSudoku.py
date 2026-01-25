"""
Complexity:
- Time  : O(1) 1 for fixed size, n² for dynamic size
- Space : O(1) 1 for fixed size, n² for dynamic size
"""
from typing import List


class Solution:
    # Runtime: 11ms
    # Memory Usage: 19.45MB
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = {}
        col = {}
        grid = {}

        n = len(board)

        for i in range(n):
            for j in range(n):
                val = board[i][j]

                if val == ".":
                    continue

                row.setdefault(i, set())
                col.setdefault(j, set())
                grid.setdefault((i//3, j//3), set())

                if val in row[i] or val in col[j] or val in grid[(i//3, j//3)]:
                    return False
                
                row[i].add(val)
                col[j].add(val)
                grid[(i//3, j//3)].add(val)
        
        return True
                

    # Best time complexity solution (0ms)
    def isValidSudokuBestTime(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == ".":
                    continue

                box_index = (r // 3) * 3 + (c // 3)

                if (
                    val in rows[r]
                    or val in cols[c]
                    or val in boxes[box_index]
                ):
                    return False

                rows[r].add(val)
                cols[c].add(val)
                boxes[box_index].add(val)

        return True

    # Best memory complexity solution (16.9MB)
    def isValidSudokuBestMemory(self, board: List[List[str]]) -> bool:
        columns_seen = [set() for i in range(9)]
        mini_grid_seen = [set() for i in range(9)]
        # 2, 5, 8
        end_mini_grid = [2 ,5 ,8]
        for row in range(len(board)):
            current_row = board[row]
            row_seen = set()
            for i, number in enumerate(current_row):
                column_seen = columns_seen[i]
                if number == ".":
                    continue
                if number in row_seen:
                    return False
                if number in column_seen:
                    return False
                column_seen.add(number)
                row_seen.add(number)

                grid_index = (row // 3) * 3 + i // 3
                grid_seen = mini_grid_seen[grid_index]
                ## update mini grid:
                if number in grid_seen:
                    return False
                grid_seen.add(number)

        return True


if __name__ == "__main__":
    s = Solution()

    print(s.isValidSudoku(
        [["5","3",".",".","7",".",".",".","."]
        ,["6",".",".","1","9","5",".",".","."]
        ,[".","9","8",".",".",".",".","6","."]
        ,["8",".",".",".","6",".",".",".","3"]
        ,["4",".",".","8",".","3",".",".","1"]
        ,["7",".",".",".","2",".",".",".","6"]
        ,[".","6",".",".",".",".","2","8","."]
        ,[".",".",".","4","1","9",".",".","5"]
        ,[".",".",".",".","8",".",".","7","9"]]
    )) # True

    print(s.isValidSudoku(
        [["8","3",".",".","7",".",".",".","."]
        ,["6",".",".","1","9","5",".",".","."]
        ,[".","9","8",".",".",".",".","6","."]
        ,["8",".",".",".","6",".",".",".","3"]
        ,["4",".",".","8",".","3",".",".","1"]
        ,["7",".",".",".","2",".",".",".","6"]
        ,[".","6",".",".",".",".","2","8","."]
        ,[".",".",".","4","1","9",".",".","5"]
        ,[".",".",".",".","8",".",".","7","9"]]
    )) # False
