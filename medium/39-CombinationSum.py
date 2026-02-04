"""
Complexity:
- Time  : O(2^(t/m)) t is target, m is minimum value in array
- Space : O(t/m)
"""
from typing import List


class Solution:
    # Runtime: 3ms
    # Memory Usage: 19.76MB
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        results = []
        candidates.sort()

        def backtrack(start_idx, current_sum, path):
            if current_sum == target:
                results.append(list(path))
                return

            for i in range(start_idx, len(candidates)):
                if current_sum + candidates[i] > target:
                    break

                # Action
                path.append(candidates[i])
                
                backtrack(i, current_sum + candidates[i], path)

                path.pop()

        backtrack(0, 0, [])
        return results

    # Best time complexity solution (0ms)
    def combinationSumBestTime(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        def dp(i,target):
            if target<0:
                return []
            elif target == 0:
                return [[]]

            res = []
            for j in range(i,len(candidates)):
                num = candidates[j]
                if target-num<0:
                    break
                comb = dp(j,target-num)
                for each in comb:
                    res.append([num] + each)
            
            return res
        
        return dp(0,target)

    # Best memory complexity solution (16.8MB)
    def combinationSumBestMemory(self, candidates: List[int], target: int) -> List[List[int]]:
        def ans(a, n, i, s, l, m):
            if i>=n or s<0:
                return
            if s==0:
                m.append(l.copy())
                return
            
            l.append(a[i])
            ans(a, n, i, s-a[i], l, m)
            l.pop()
            ans(a, n, i+1, s, l, m)

        m=[]
        ans(candidates, len(candidates), 0, target, [], m)
        return(m)


if __name__ == "__main__":
    s = Solution()

    print(s.combinationSum([2,3,6,7], 7)) # [[2,2,3],[7]]
    print(s.combinationSum([2,3,5], 8)) # [[2,2,2,2],[2,3,3],[3,5]]
    print(s.combinationSum([2], 1)) # []
