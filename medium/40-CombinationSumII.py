"""
Complexity:
- Time  : O(2^n * n)
- Space : O(n)
"""
from typing import List


class Solution:
    # Runtime: 3ms
    # Memory Usage: 19.78MB
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        results = []
        candidates.sort()

        def backtrack(start_idx, current_sum, path):
            if current_sum == target:
                results.append(list(path))
                return
            
            for i in range(start_idx, len(candidates)):
                if i > start_idx and candidates[i] == candidates[i - 1]:
                    continue
                if current_sum + candidates[i] > target:
                    break

                path.append(candidates[i])
                backtrack(i + 1, current_sum + candidates[i], path)
                path.pop()

        backtrack(0, 0, [])
        return results

    # Best time complexity solution (1ms)
    def combinationSum2BestTime(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()        
        result = []
        self.backtrack(candidates, target, 0, [], result)
        return result
    def backtrack(self, candidates, target, index, path, result):
        if target == 0:
            result.append(path[:])
            return
        for i in range(index, len(candidates)):
            if i > index and candidates[i] == candidates[i - 1]:
                continue
            if candidates[i] > target:
                break
            path.append(candidates[i])
            self.backtrack(candidates, target - candidates[i], i + 1, path, result)
            path.pop()

    # Best memory complexity solution (17MB)
    def __init__(self):
        self.result = []
    def combinationSum2BestMemory(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()    
        self.dfs(candidates, 0, 0, [], target)
        return self.result
    
    def dfs(self, nums, start, total, cur, target):
        if total > target:
            return
        if total == target:
            self.result.append(cur.copy())
            return
        for i in range (start, len(nums)):
            if i > start and nums[i] == nums[i-1]:
                continue
            self.dfs( nums, i + 1, total + nums[i], cur + [nums[i]], target)


if __name__ == "__main__":
    s = Solution()

    print(s.combinationSum2([10,1,2,7,6,1,5], 8)) # [[1,1,6], [1,2,5], [1,7], [2,6]]
    print(s.combinationSum2([2,5,2,1,2], 5)) # [[1,2,2], [5]]
