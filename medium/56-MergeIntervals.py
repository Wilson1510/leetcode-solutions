"""
Complexity:
- Time  : O(n log(n))
- Space : O(n)
"""
from typing import List


class Solution:
    # Runtime: 4ms
    # Memory Usage: 22.5MB
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        result = [intervals[0]]

        for i in range(1, len(intervals)):
            before = result[-1]
            current = intervals[i]

            if before[1] >= current[0]:
                result[-1] = [before[0], max(before[1], current[1])]
            else:
                result.append(current)
        return result

    # Best time complexity solution (0ms)
    def mergeBestTime(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key = lambda x: x[0])
        ans = []

        for interval in intervals:
            if not ans or ans[-1][1] < interval[0]:
                ans.append(interval)
            else:
                ans[-1][1] = max(ans[-1][1], interval[1])

        return ans

    # Best memory complexity solution (19.1MB)
    def mergeBestMemory(self, intervals: List[List[int]]) -> List[List[int]]:
        '''
        Iterate through a nested for loop, comparing an element with every other element
        Check if [1] index is greater than [0] index, and if it is then modify the element and merge
        '''
        #result = [[] for _ in range(len(intervals))]]
        result = []
        indexMerged = set()
        numMerged = 0

        while True:
            for i in range(len(intervals)):
                if i in indexMerged:
                    continue
                for j in range(len(intervals)):
                    if j in indexMerged or j == i:
                        continue
                    if intervals[i][0] <= intervals[j][1] and intervals[i][1] >= intervals[j][0] and intervals[i][0] <= intervals[j][0]:
                        print(i)
                        print(f"{intervals[i]} and {intervals[j]}")
                        intervals[i][1] = max(intervals[j][1], intervals[i][1])
                        indexMerged.add(j)
                        numMerged+=1
            if numMerged == 0: break
            numMerged = 0
        
        #print(indexMerged)
        for i in range(len(intervals)):
            if i not in indexMerged:
                result.append(intervals[i])

        return result


if __name__ == "__main__":
    s = Solution()

    print(s.merge([[1,3],[2,6],[8,10],[15,18]])) # [[1,6],[8,10],[15,18]]
    print(s.merge([[1,4],[4,5]])) # [[1,5]]
    print(s.merge([[4,7],[1,4]])) # [[1,7]]
    print(s.merge([[1, 3]])) # [[1, 3]]
    print(s.merge([[1,4],[0,2],[3,5]])) # [[0, 5]]
    print(s.merge([[1,4],[0,0]])) # [[0,0],[1,4]]
    print(s.merge([[2,3],[4,5],[6,7],[8,9],[1,10]])) # [[1, 10]]
