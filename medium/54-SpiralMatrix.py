"""
Complexity:
- Time  : O(mn)
- Space : O(1)
"""
from typing import List


class Solution:
    # Runtime: 0ms
    # Memory Usage: 19.3MB
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        # Inisialisasi 4 batas
        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1

        while left <= right and top <= bottom:
            # 1. Jalan ke Kanan (di baris top)
            for j in range(left, right + 1):
                res.append(matrix[top][j])
            top += 1  # Tembok atas turun

            # 2. Jalan ke Bawah (di kolom right)
            for i in range(top, bottom + 1):
                res.append(matrix[i][right])
            right -= 1  # Tembok kanan masuk ke kiri

            # Cek apakah masih ada baris/kolom tersisa (penting untuk matriks persegi
            # panjang)
            if not (left <= right and top <= bottom):
                break

            # 3. Jalan ke Kiri (di baris bottom)
            for j in range(right, left - 1, -1):
                res.append(matrix[bottom][j])
            bottom -= 1  # Tembok bawah naik

            # 4. Jalan ke Atas (di kolom left)
            for i in range(bottom, top - 1, -1):
                res.append(matrix[i][left])
            left += 1  # Tembok kiri masuk ke kanan

        return res

    # Best time complexity solution (0ms)
    def spiralOrderBestTime(self, matrix: List[List[int]]) -> List[int]:

        result = []

        top = 0
        bottom = len(matrix) - 1
        left = 0
        right = len(matrix[0]) - 1

        while top <= bottom and left <= right:

            # 1️⃣ Move Right
            for j in range(left, right + 1):
                result.append(matrix[top][j])
            top += 1

            # 2️⃣ Move Down
            for i in range(top, bottom + 1):
                result.append(matrix[i][right])
            right -= 1

            # 3️⃣ Move Left
            if top <= bottom:
                for j in range(right, left - 1, -1):
                    result.append(matrix[bottom][j])
                bottom -= 1

            # 4️⃣ Move Up
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    result.append(matrix[i][left])
                left += 1

        return result

    # Best memory complexity solution (16.9MB)
    def spiralOrderBestMemory(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []

        ret = []
        while matrix:

            ret += matrix.pop(0)

            if matrix and matrix[0]:
                for r in matrix:
                    ret.append(r.pop())

            if matrix and matrix[0]:
                ret += matrix.pop()[::-1]

            if matrix and matrix[0]:
                for r in matrix[::-1]:
                    ret.append(r.pop(0))
        return ret


if __name__ == "__main__":
    s = Solution()
    print(s.spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))  # [1,2,3,6,9,8,7,4,5]
    print(s.spiralOrder([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]))
    # [1,2,3,4,8,12,11,10,9,5,6,7]
