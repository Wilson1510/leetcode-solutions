"""
Complexity:
- Time  : O(n)
- Space : O(1)
"""


class Solution:
    # Runtime: 0ms
    # Memory Usage: 19.27MB
    def numDecodings(self, s: str) -> int:
        n = len(s)

        next1 = 1  # dp[i+1]
        next2 = 0  # dp[i+2]

        for i in range(n - 1, -1, -1):
            curr = 0

            if s[i] != '0':
                curr = next1

                if i + 1 < n and (s[i] == '1' or (s[i] == '2' and s[i + 1] <= '6')):
                    curr += next2 if i + 2 <= n else 1

            next2 = next1
            next1 = curr

        return next1

    # Best time complexity solution (0ms)
    def numDecodingsBestTime(self, s: str) -> int:
        n=len(s)
        dp=[-1]*(n+1)
        ans=0
        def decode(i):
            if i==0:
                return 1
            if i==1:
                if 1<=int(s[0])<=9:
                    return 1
                else:
                    return 0
            if dp[i]!=-1:
                return dp[i]
            ways=0
            if 1<=int(s[i-1])<=9:
                ways+=decode(i-1)
            if 10<=int(s[i-2:i])<=26:
                ways+=decode(i-2)
            dp[i]=ways
            return dp[i]
        return decode(n)

    # Best memory complexity solution (16.8MB)
    def numDecodingsBestMemory(self, s: str) -> int:
        N = len(s)
        
        if s[0] == '0':
            return 0
        
        if N == 1:
            return 1
        
        dp = N*[1]
        
        for i in range(1,N):
            
            if int(s[i]) == 0:
                 if int(s[i-1]) == 0:
                    return 0
                 else:
                    if int(s[i-1]) <=2:
                        dp[i] = 1 * (dp[i-2] if i-2>=0 else 1)
                    else:
                        return 0                
            else:
                assert s[i] != '0'
                dp[i] = dp[i-1]
                
                if (int(s[i-1]) == 2 and int(s[i]) <= 6) or (int(s[i-1]) == 1):
                    dp[i] += (dp[i-2] if i-2>=0 else 1)
                    
        return dp[-1]


if __name__ == "__main__":
    s = Solution()

    print(s.numDecodings("12")) # 2
    print(s.numDecodings("226")) # 3
    print(s.numDecodings("06")) # 0
    print(s.numDecodings("75123726")) # 6
