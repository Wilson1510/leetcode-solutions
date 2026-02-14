"""
Complexity:
- Time  : O(n*amount)
- Space : O(amount)
"""
from typing import List
from math import gcd


class Solution:
    # Runtime: 459ms
    # Memory Usage: 19.54MB
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0: return 0

        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for i in range(1, amount + 1):
            for coin in coins:
                if i >= coin:
                    dp[i] = min(dp[i], dp[i-coin] + 1)
        return dp[amount] if dp[amount] != float('inf') else -1

    # Best time complexity solution (9ms)
    def coinChangeBestTime(self, coins: List[int], amount: int) -> int:
        T = amount
        if T < 1: return 0
        C = coins
        n = len(C)
        if n < 2: return -1 if T % C[0] else T // C[0]
        g = C[0]
        for c in C[1:]: g = gcd(g, c)
        if T % g: return -1
        if T in C: return 1
        if n < 3:
            a, b = (C[0], C[1]) if C[0] < C[1] else (C[1], C[0])
            nb, rem = divmod(T, b)
            while nb >= 0:
                if not rem % a: return nb + rem // a
                nb -= 1
                rem += b
            return -1
        C.sort()
        a, b = C[0], C[1]
        ga = gcd(a, b)
        ar = a // ga
        if n < 4:
            c, best = C[2], T + 1
            if ar > 1:
                inv = pow(b // ga, -1, ar)
                for nc in range(T // c, -1, -1):
                    if nc >= best: break
                    rem = T - nc * c
                    if rem % ga: continue
                    nb = rem // b - (rem // b - (rem // ga * inv) % ar) % ar
                    if nb >= 0:
                        v = nc + nb + (rem - nb * b) // a
                        if v < best: best = v
            else:
                for nc in range(T // c, -1, -1):
                    if nc >= best: break
                    rem = T - nc * c
                    nb = rem // b
                    v = nc + nb + (rem - nb * b) // a
                    if v < best: best = v
            return best if best <= T else -1
        r = 1 << T
        s = 0
        if n < 5:
            c, d = C[2], C[3]
            while r:
                s += 1; r = r >> a | r >> b | r >> c | r >> d
                if r & 1: return s
        elif n < 6:
            c, d, e = C[2], C[3], C[4]
            while r:
                s += 1; r = r >> a | r >> b | r >> c | r >> d | r >> e
                if r & 1: return s
        elif n < 7:
            c, d, e, f = C[2], C[3], C[4], C[5]
            while r:
                s += 1; r = r >> a | r >> b | r >> c | r >> d | r >> e | r >> f
                if r & 1: return s
        else:
            while r:
                s += 1; x = 0
                for c in C: x |= r >> c
                if x & 1: return s
                r = x
        return -1

    # Best memory complexity solution (17.28MB)
    def coinChangeBestMemory(self, coins: List[int], amount: int) -> int:
        dp = [amount+1]*(amount+1)

        dp[0]=0

        for a in range(1,amount+1):
            for c in coins:
                if a-c>=0:
                    dp[a] = min(dp[a],1+dp[a-c])
        return dp[amount] if dp[amount]!=amount+1 else -1


if __name__ == "__main__":
    s = Solution()

    print(s.coinChange([1, 2, 5], 11)) # 3
    print(s.coinChange([2], 3)) # -1
    print(s.coinChange([1], 0)) # 0
    print(s.coinChangeBest([1, 3, 4], 6)) # 2
    print(s.coinChange([7, 2, 5], 27)) # 5
