"""
Complexity:
- Time  : O(mn)
- Space : O(mn)
"""
from typing import List


class Solution:
    # Runtime: 3ms
    # Memory Usage: 22.26MB
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        edges = []
        for i in range(m):
            if board[i][0] == 'O':
                edges.append((i, 0))
            if board[i][n - 1] == 'O':
                edges.append((i, n - 1))

        for j in range(n):
            if board[0][j] == 'O':
                edges.append((0, j))
            if board[m - 1][j] == 'O':
                edges.append((m - 1, j))
        
        for edge in edges:
            stack = [edge]
            while stack:
                r, c = stack.pop()
                for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                    mr, nc = r + dr, c + dc
                    if 0 < mr < m - 1 and 0 < nc < n - 1 and board[mr][nc] == 'O':
                        board[mr][nc] = 'T'
                        stack.append((mr, nc))

        for i in range(1, m - 1):
            for j in range(1, n - 1):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'T':
                    board[i][j] = 'O'

    # Best time complexity solution (0ms)
    def solveBestTime(self, board: List[List[str]]) -> None:
        if not board or not board[0]:
            return
        
        rows, cols = len(board), len(board[0])
        
        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != 'O':
                return
            board[r][c] = 'T'  
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
        
        for i in range(rows):
            if board[i][0] == 'O':
                dfs(i, 0)
            if board[i][cols - 1] == 'O':
                dfs(i, cols - 1)
        
        for j in range(cols):
            if board[0][j] == 'O':
                dfs(0, j)
            if board[rows - 1][j] == 'O':
                dfs(rows - 1, j)
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O':
                    board[r][c] = 'X' 
                elif board[r][c] == 'T':
                    board[r][c] = 'O'  

    # Best memory complexity solution (20.5MB)
    def solveBestMemory(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        def dfs(i, j, visited):
            visited.add((i,j))
            for di, dj in [(0,1), (0,-1), (1,0), (-1,0)]:
                newi, newj = i + di, j + dj
                if 0 <= newi < n and 0 <= newj < m and board[newi][newj] == "O" and (newi, newj) not in visited:
                    visited = dfs(newi, newj, visited)
            return visited

        n, m = len(board), len(board[0])
        not_surrounded = set()

        for i in range(n):
            if board[i][0] == "O":
                not_surrounded = dfs(i, 0, not_surrounded)
            if board[i][m-1] == "O":
                not_surrounded = dfs(i, m-1, not_surrounded)
            
        for j in range(m):
            if board[0][j] == "O":
                not_surrounded = dfs(0, j, not_surrounded)
            if board[n-1][j] == "O":
                not_surrounded = dfs(n-1, j, not_surrounded)
        
        for i in range(n):
            for j in range(m):
                if (i,j) in not_surrounded:
                    board[i][j] = "O"
                else:
                    board[i][j] = "X"
        return board


if __name__ == "__main__":
    s = Solution()

    print(s.solve([
        ["X","X","X","X"],
        ["X","O","O","X"],
        ["X","X","O","X"],
        ["X","O","X","X"]
    ])) # [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
    print(s.solve([["X"]])) # [["X"]]
    print(s.solve([
        ["X","O","O","X","X","X","O","X","O","O"],
        ["X","O","X","X","X","X","X","X","X","X"],
        ["X","X","X","X","O","X","X","X","X","X"],
        ["X","O","X","X","X","O","X","X","X","O"],
        ["O","X","X","X","O","X","O","X","O","X"],
        ["X","X","O","X","X","O","O","X","X","X"],
        ["O","X","X","O","O","X","O","X","X","O"],
        ["O","X","X","X","X","X","O","X","X","X"],
        ["X","O","O","X","X","O","X","X","O","O"],
        ["X","X","X","O","O","X","O","X","X","O"]
    ]))
    """
    [
        ["X","O","O","X","X","X","O","X","O","O"],
        ["X","O","X","X","X","X","X","X","X","X"],
        ["X","X","X","X","X","X","X","X","X","X"],
        ["X","X","X","X","X","X","X","X","X","O"],
        ["O","X","X","X","X","X","X","X","X","X"],
        ["X","X","X","X","X","X","X","X","X","X"],
        ["O","X","X","X","X","X","X","X","X","O"],
        ["O","X","X","X","X","X","X","X","X","X"],
        ["X","X","X","X","X","X","X","X","O","O"],
        ["X","X","X","O","O","X","O","X","X","O"]
    ]
    """
