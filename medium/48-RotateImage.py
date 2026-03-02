"""
Complexity:
- Time  : O(n^2)
- Space : O(1)
"""
from typing import List


class Solution:
    # Runtime: 0ms
    # Memory Usage: 19.48MB
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for row in matrix:
            row.reverse()

    # Best time complexity solution (0ms)
    def rotateBestTime(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix[0])
        for i in range(n//2 + n % 2):
            for j in range(n//2):
                temp = matrix[n - 1 - j][i]
                matrix[n - 1 - j][i] = matrix[n - 1 - i][n - 1 - j]
                matrix[n - 1 - i][n - 1 - j] = matrix[j][n - 1 - i]
                matrix[j][n - 1 - i] = matrix[i][j]
                matrix[i][j] = temp

    # Best memory complexity solution (16.8MB)
    def rotateBestMemory(self, matrix: List[List[int]]) -> None:
        #  transpose+mirror image
        n = len(matrix)
        for i in range(n):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        st, ed = 0, n-1
        while st < ed:
            for i in range(n):
                matrix[i][st], matrix[i][ed] = matrix[i][ed], matrix[i][st]
            st = st + 1
            ed = ed - 1


if __name__ == "__main__":
    s = Solution()
    s.rotate([[1, 2, 3], [4, 5, 6], [7, 8, 9]])  # [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
    s.rotate([[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]])
    # [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
