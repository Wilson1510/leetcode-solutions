"""
Complexity:
- Time  : O(1)
- Space : O(1)
"""


class Solution:
    # Runtime: 0ms
    # Memory Usage: 19.2MB
    def getSum(self, a: int, b: int) -> int:
        MASK = 0xffffffff
        MAX_INT = 0x7fffffff

        while b != 0:
            carry = (a & b) << 1
            a = (a ^ b) & MASK
            b = carry & MASK

        return a if a <= MAX_INT else ~(a ^ MASK)

    # Best time complexity solution (0ms)
    def getSumBestTime(self, a: int, b: int) -> int:
        mask = 0xffffffff

        while (b & mask):
            carry = (a & b) << 1
            a = a ^ b
            b = carry

        return (a & mask) if b > 0 else a

    # Best memory complexity solution (17MB)
    def getSumBestMemory(self, a: int, b: int) -> int:
        m=0xFFFFFFFF
        n=0x7FFFFFFF
        while b!=0:
            c = (a&b)<<1
            a = (a^b) & m 
            b = c & m
        return a if a <= n else ~(a^m)


if __name__ == "__main__":
    s = Solution()

    print(s.getSum(1, 2))  # 3
    print(s.getSum(2, 3))  # 5
    print(s.getSum(20, 30))  # 50
    print(s.getSum(1, -1))  # 0
