"""
Complexity:
- Time  : O(log n)
- Space : O(1)
"""


class Solution:
    # Runtime: 0ms
    # Memory Usage: 19.22MB
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            n &= (n - 1)
            count += 1
        return count

    # Best time complexity solution (0ms)
    def hammingWeightBestTime(self, n: int) -> int:
        res = 0
        for _ in range(32):
            bit = n & 1
            if bit == 1:
                res += 1
            n >>= 1
        return res

    # Best memory complexity solution (16.6MB)
    def hammingWeightBestMemory(self, n: int) -> int:
        # use while loop while n is not 0

        # and then check if n & 1 == 1 then update number of bits

        # shift it to the right by 1 (>>)

        result = 0

        while n != 0:
            if n & 1 == 1:
                result += 1
            n >>= 1

        return result


if __name__ == "__main__":
    s = Solution()

    print(s.hammingWeight(11))  # 3
    print(s.hammingWeight(128))  # 1
    print(s.hammingWeight(2147483645))  # 30
