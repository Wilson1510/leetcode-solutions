"""
Complexity:
- Time  : O(mn)
- Space : O(mn)
"""
from typing import List, Tuple


class Solution:
    # Runtime: 35ms
    # Memory Usage: 22.3MB
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        pacific, atlantic = set(), set()

        def can_flow(i, j, visited):
            visited.add((i, j))
            for di, dj in [(0, -1), (-1, 0), (0, 1), (1, 0)]:
                mi, nj = i + di, j + dj
                if 0 <= mi < m and 0 <= nj < n and heights[mi][nj] >= heights[i][j] and (mi, nj) not in visited:
                    can_flow(mi, nj, visited)

        for i in range(m):
            can_flow(i, 0, pacific)
            can_flow(i, n - 1, atlantic)

        for j in range(n):
            can_flow(0, j, pacific)
            can_flow(m - 1, j, atlantic)
        return list(pacific & atlantic)

    # Best time complexity solution (21ms)
    def pacificAtlanticBestTime(self, heights: List[List[int]]) -> List[List[int]]:
        nb_rows = len(heights)
        nb_cols = len(heights[0])

        start = [(i, 0) for i in range(nb_rows)]
        start.extend([ (0, i) for i in range(nb_cols)])
        # print ("start", start)
        pacific = self.getHighestOrEqualValue(heights, start)
        # print (pacific)
        
        start = [(i, nb_cols-1) for i in range(nb_rows)]         
        start.extend([(nb_rows -1, i) for i in range(nb_cols)])
        # print ("start", start)

        atlantic = self.getHighestOrEqualValue(heights, start)
        res = []
        for i,j in pacific:
            if (i,j) in atlantic:
                res.append([i,j ])
        return res
    
    def getHighestOrEqualValue(self, heights: List[List[int]], start: List[Tuple[int, int]]) -> set[Tuple[int, int]]:
        done = set()                
        while len(start) > 0:
            i,j = start.pop()
            if (i,j) in done:
                continue
            done.add((i,j))

            if i > 0 and heights[i][j] <= heights[i-1][j]:
                start.append([i-1, j])
            if i +1 < len(heights) and heights[i][j] <= heights[i+1][j]:
                start.append([i+1, j])
            if j > 0 and heights[i][j] <= heights[i][j-1]:
                start.append([i, j-1])
            if j +1 < len(heights[i]) and heights[i][j] <= heights[i][j+1]:
                start.append([i, j+1])
            
        return done 

    # Best memory complexity solution (18.2MB)
    def pacificAtlanticBestMemory(self, heights: List[List[int]]) -> List[List[int]]:
        res = []
        m = len(heights)
        n = len(heights[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        pacific = atlantic = False

        def backtrack(prev,r,c):
            nonlocal pacific,atlantic
            if r >= m or c >= n:
                atlantic = True
                return
            if r < 0 or c < 0:
                pacific = True
                return
            
            if prev < heights[r][c]:
                return

            tmp = heights[r][c]
            heights[r][c] = float('inf')
            for dx, dy in directions:
                backtrack(tmp, r + dx, c + dy)
                if pacific and atlantic:
                    break
            heights[r][c]=tmp


        for row in range(m):
            for col in range(n):
                pacific = False
                atlantic = False
                backtrack(float('inf'),row,col) 
                if pacific and atlantic:
                    res.append([row,col])
        return res


if __name__ == "__main__":
    s = Solution()

    print(s.pacificAtlantic(
        [
            [1,2,2,3,5],
            [3,2,3,4,4],
            [2,4,5,3,1],
            [6,7,1,4,5],
            [5,1,1,2,4]
        ]
    )) # [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]

    print(s.pacificAtlantic([[1]])) # [[0, 0]]
