"""
Complexity:
- Time  : O(mn)
- Space : O(mn)
"""
from typing import List
from collections import deque


class Solution:
    # Runtime: 3ms
    # Memory Usage: 19.44MB
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        queue = deque([])
        fresh_oranges = 0
        
        # 1. Persiapan awal: Masukkan semua yang busuk & hitung yang segar
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append((i, j))
                elif grid[i][j] == 1:
                    fresh_oranges += 1
        
        # Jika tidak ada jeruk segar dari awal, waktu yang dibutuhkan 0
        if fresh_oranges == 0: return 0
        
        minutes = 0
        
        # 2. Proses BFS per "level" (per menit)
        while queue and fresh_oranges > 0:
            minutes += 1
            # Ambil jumlah jeruk busuk SAAT INI saja (level ini)
            for _ in range(len(queue)):
                r, c = queue.popleft()
                
                for i, j in [(0, -1), (-1, 0), (0, 1), (1, 0)]:
                    mr, nc = r + i, c + j
                    
                    # Jika tetangga adalah jeruk segar
                    if 0 <= mr < m and 0 <= nc < n and grid[mr][nc] == 1:
                        grid[mr][nc] = 2 # Buat jadi busuk
                        fresh_oranges -= 1 # Kurangi stok jeruk segar
                        queue.append((mr, nc))
        
        # 3. Cek apakah masih ada jeruk segar yang tersisa (tidak terjangkau)
        return minutes if fresh_oranges == 0 else -1

    # Best time complexity solution (0ms)
    def orangesRottingBestTime(self, grid: List[List[int]]) -> int:
        res = 0
        m = len(grid); 
        n = len(grid[0])

        vis = [0]

        q = deque()

        row = [-1,0,1,0]
        col = [0,1,0,-1]

        for i in range(m):
            for j in range(n):
                if grid[i][j] ==2:
                    q.append((i,j, 0))

        while q:
            r, c,t  = q.popleft()
            res = max(t, res)

            for i in range(4):
                rr = r+ row[i]
                cc = c + col[i]

                if (rr >=0 and rr<m and cc>=0 and cc<n and grid[rr][cc] ==1):
                    grid[rr][cc] =2
                    q.append((rr, cc, t+1))
        

        for i in range(m):
            for j in range(n):
                if( grid[i][j] ==1):
                    return -1

        
        return res

    # Best memory complexity solution (16.9MB)
    def orangesRottingBestMemory(self, grid: List[List[int]]) -> int:
        need_rot = 0
        q = deque([])
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    q.append((i, j))
                if grid[i][j] == 1:
                    need_rot += 1
        if need_rot == 0:
            return 0
        
        count = -1
        while q:
            for _ in range(len(q)):
                curr_i, curr_j = q.popleft()

                dic = [[0, 1], [1, 0], [-1, 0], [0, -1]]

                for r, c in dic:
                    nxt_r, nxt_c = curr_i+r, curr_j+c
                    if nxt_r >= 0 and nxt_c >= 0 and nxt_r < len(grid) and nxt_c < len(grid[0]):
                        if grid[nxt_r][nxt_c] == 1:
                            grid[nxt_r][nxt_c] = 2
                            need_rot -= 1
                            q.append((nxt_r, nxt_c))
            
            count += 1
        
        if need_rot > 0:
            return -1
        return count


if __name__ == "__main__":
    s = Solution()

    print(s.orangesRotting([[2,1,1],[1,1,0],[0,1,1]])) # 4
    print(s.orangesRotting([[2,1,1],[0,1,1],[1,0,1]])) # -1
    print(s.orangesRotting([[0, 2]])) # 0
