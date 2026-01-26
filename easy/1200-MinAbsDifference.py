"""
Complexity:
- Time  : O(n log(n))
- Space : O(n)
"""
from typing import List


class Solution:
    # Runtime: 43ms
    # Memory Usage: 31.4MB
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        minimum = float('inf')
        result = []
        n = len(arr)

        for i in range(n-1):
            diff = arr[i+1] - arr[i]
        
            if diff < minimum:
                minimum = diff
                result = [[arr[i], arr[i+1]]]
            elif diff == minimum:
                result.append([arr[i], arr[i+1]])
        return result

    # Best time complexity solution (0ms)
    def minimumAbsDifferenceBestTime(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        min_diff = float('inf')
        for i in range(len(arr)-1):
            current_diff = arr[i+1] - arr[i]
            if current_diff < min_diff:
                min_diff = current_diff

        answer = []

        for i in range(len(arr)-1):
            if (abs(arr[i] - arr[i+1])) <= min_diff:
                answer.append([arr[i], arr[i+1]])

        return answer

    # Best memory complexity solution (29MB)
    def minimumAbsDifferenceBestMemory(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        mindiff = float('inf')
        for i in range(len(arr)-1):
            if mindiff>arr[i+1]-arr[i]:
                mindiff = min(mindiff, arr[i+1]-arr[i])
                ans = []
            if (arr[i+1]-arr[i] ==mindiff ):
                ans.append([arr[i],arr[i+1]])
        return ans


if __name__ == "__main__":
    s = Solution()

    print(s.minimumAbsDifference([4,2,1,3])) # [[1,2],[2,3],[3,4]]
    print(s.minimumAbsDifference([1,3,6,10,15])) # [[1,3]]
    print(s.minimumAbsDifference([3,8,-10,23,19,-4,-14,27])) # [[-14,-10],[19,23],[23,27]]
