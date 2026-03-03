"""
Complexity:
- Time  : O(1)
- Space : O(1)
"""


class Solution:
    # Runtime: 52ms
    # Memory Usage: 19.06MB
    def reverseBits(self, n: int) -> int:
        res = 0
        for _ in range(32):
            res = (res << 1) | (n & 1)
            n >>= 1
        return res

    # Best time complexity solution (20ms)
    def reverseBitsBestTime(self, n: int) -> int:
        res = 0
        for i in range(32):
            res = (res << 1) | (n & 1)
            n >>= 1
        return res

    # Best memory complexity solution (17MB)
    def reverseBitsBestMemory(self, n: int) -> int:
        result = ''.join(list(bin(n))[2:][::-1])
        result = result + '0' * (32 - len(result))

        return int(result, 2)


if __name__ == "__main__":
    s = Solution()

    print(s.reverseBits(43261596))  # 964176192
    print(s.reverseBits(2147483644))  # 1073741822
