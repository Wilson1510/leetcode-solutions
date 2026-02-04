"""
Complexity:
- Time  : O(n*2^n)
- Space : O(2^n)
"""


class Solution:
    # Runtime: 7ms
    # Memory Usage: 19.36MB
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        
        def rle(digits):
            digit_list = []

            prev = None
            count = 1
            for digit in digits:
                if digit == prev:
                    count += 1
                    digit_list[-2] = str(count)
                else:
                    count = 1
                    prev = digit
                    digit_list.append(str(count))
                    digit_list.append(digit)
            return "".join(digit_list)
        return rle(self.countAndSay(n - 1))

    # Best time complexity solution (1ms)
    def countAndSayBestTime(self, n: int) -> str:
        s = "1"

        for _ in range(n - 1):
            res = []
            i = 0

            while i < len(s):
                count = 1
                while i + 1 < len(s) and s[i] == s[i + 1]:
                    i += 1
                    count += 1
                res.append(str(count))
                res.append(s[i])
                i += 1

            s = "".join(res)

        return s

    # Best memory complexity solution (17MB)
    def countAndSayBestMemory(self, n: int) -> str:
        current_string = "1"
        for _ in range(n - 1):
            next_string = ""
            j = 0
            k = 0
            while j < len(current_string):
                while (
                    k < len(current_string)
                    and current_string[k] == current_string[j]
                ):
                    k += 1
                next_string += str(k - j) + current_string[j]
                j = k
            current_string = next_string
        return current_string


if __name__ == "__main__":
    s = Solution()

    print(s.countAndSay(4)) # 1211
    print(s.countAndSay(1)) # 1
