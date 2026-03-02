"""
Complexity:
- Time  : O(mn)
- Space : O(1)
"""
from typing import List


class Solution:
    # Runtime: 5ms
    # Memory Usage: 20.23MB
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        first_row_has_zero = any(matrix[0][j] == 0 for j in range(n))
        first_col_has_zero = any(matrix[i][0] == 0 for i in range(m))

        # Gunakan baris & kolom pertama untuk menandai baris/kolom mana yang harus nol
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        # Isi nol berdasarkan penanda di baris & kolom pertama
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        # Tangani baris pertama sendiri
        if first_row_has_zero:
            for j in range(n):
                matrix[0][j] = 0

        # Tangani kolom pertama sendiri
        if first_col_has_zero:
            for i in range(m):
                matrix[i][0] = 0

    # Best time complexity solution (0ms)
    def setZeroesBestTime(self, matrix: List[List[int]]) -> None:
        m = len(matrix)
        n = len(matrix[0])

        row = [0] * m
        col = [0] * n

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    row[i] = 1
                    col[j] = 1

        for i in range(m):
            for j in range(n):
                if row[i] == 1 or col[j] == 1:
                    matrix[i][j] = 0

        return matrix

    # Best memory complexity solution (17.4MB)
    def setZeroesBestMemory(self,matrix) -> None: 
        rws=len(matrix)
        clm=len(matrix[0])
        rwz= [0]*rws
        clz=[0]*clm
        for rw in range(rws):
            for cm in range(clm):
                if matrix[rw][cm] == 0 :
                    rwz[rw]=1
                    clz[cm]=1
        for rw in range(rws):
            for cm in range(clm):
                if rwz[rw] or clz[cm]: 
                    matrix[rw][cm]=0


if __name__ == "__main__":
    s = Solution()

    s.setZeroes([[1, 1, 1], [1, 0, 1], [1, 1, 1]])  # [[1,0,1],[0,0,0],[1,0,1]]
    s.setZeroes([[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]])
    # [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
