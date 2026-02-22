"""
Complexity:
- Time  : O(mn)
- Space : O(mn)
"""
from typing import List


class Solution:
    # Runtime: 233ms
    # Memory Usage: 79.3MB
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        def mark_cell(i, j):
            grid[i][j] = "0"
            for mi, nj in [(0, -1), (-1, 0), (0, 1), (1, 0)]:
                if 0 <= i + mi < m and 0 <= j + nj < n and grid[i + mi][j + nj] == "1":
                    mark_cell(i + mi, j + nj)

        count = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    mark_cell(i, j)
                    count += 1
        return count

    # Best time complexity solution (13ms)
    def numIslandsBestTime(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        m, n = len(grid), len(grid[0])
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    res += 1
                    stack = [(i, j)]
                    grid[i][j] = '0'  
                    while stack:
                        x, y = stack.pop()
                        nx = x + 1
                        if nx < m and grid[nx][y] == '1':
                            grid[nx][y] = '0'
                            stack.append((nx, y))
                        nx = x - 1
                        if nx >= 0 and grid[nx][y] == '1':
                            grid[nx][y] = '0'
                            stack.append((nx, y))
                        ny = y + 1
                        if ny < n and grid[x][ny] == '1':
                            grid[x][ny] = '0'
                            stack.append((x, ny))
                        ny = y - 1
                        if ny >= 0 and grid[x][ny] == '1':
                            grid[x][ny] = '0'
                            stack.append((x, ny))
        return res

    # Best memory complexity solution (18.8MB)
    def numIslandsBestMemory(self, grid: List[List[str]]) -> int:
        #number of rows and number of columns
        m,n = len(grid),len(grid[0])

        #marks entire land into water
        def dfs(i,j):
            if i<0 or i>=m or j<0 or j>=n or grid[i][j]!='1':
                return
            else:
                grid[i][j] = '0'
                dfs(i,j+1) #right
                dfs(i+1,j)#bottom
                dfs(i,j-1) #left
                dfs(i-1,j)#bottom

        num_islands = 0
        for i in range(m):
            for j in range(n):
                #if grid ith and jth index is equal to 1
                if grid[i][j] == '1':
                    num_islands +=1 #increase by one
                    dfs(i,j) #turn into water
        return num_islands


if __name__ == "__main__":
    s = Solution()

    print(s.numIslands(
        [
            ["1","1","1","1","0"],
            ["1","1","0","1","0"],
            ["1","1","0","0","0"],
            ["0","0","0","0","0"]
        ]
    )) # 1
    print(s.numIslands(
        [
            ["1","1","0","0","0"],
            ["1","1","0","0","0"],
            ["0","0","1","0","0"],
            ["0","0","0","1","1"]
        ]
    )) # 3
