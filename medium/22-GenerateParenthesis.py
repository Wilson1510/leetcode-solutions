"""
Complexity:
- Time  : O(C(n) x n)
- Space : O(C(n) x n)
"""
from typing import List


class Solution:
    # Runtime: 0ms
    # Memory Usage: 19.41MB
    def generateParenthesis(self, n: int) -> List[str]:
        def dfs(left, right, s):
            if len(s) == 2 * n:
                result.append(s)
                return
            if left < n:
                dfs(left + 1, right, s + "(")
            if right < left:
                dfs(left, right + 1, s + ")")

        result = []
        dfs(0, 0, "")
        return result


    # Best time complexity solution (0ms)
    def generateParenthesisBestTime(self, n: int) -> List[str]:
        all_combinattions = [set() for _ in range(n+1)] 
        all
        # n = 1
        all_combinattions[0].add("")
        for i in range(1, n+1):
 
            for j in range(i):
                for l1 in all_combinattions[j]:
                    for l2 in all_combinattions[i-1-j]:
                        all_combinattions[i].add('('+l1+')'+l2)

        
        return list(all_combinattions[n])

    # Best memory complexity solution (17.1MB)
    def generateParenthesisBestSolution(self, n: int) -> List[str]:
        res = []
        
        def dfs(i, combs, left_params, right_params):
            if i == 2*n:
                res.append(''.join(combs))
                return

            for edge in '()': 
                if right_params > 0 and edge == ')':
                    if right_params-1 >= left_params:
                        combs.append(')')
                        dfs(i+1, combs, left_params, right_params-1)
                        combs.pop()
                if left_params > 0 and edge == '(':
                    combs.append('(')
                    dfs(i+1, combs, left_params-1, right_params)
                    combs.pop()

        dfs(0, [], n, n)


if __name__ == "__main__":
    s = Solution()
    print(s.generateParenthesis(3)) # ["((()))","(()())","(())()","()(())","()()()"]
    print(s.generateParenthesis(1)) # ["()"]
