"""
Complexity:
- Time  : O(n log(n))
- Space : O(n)
"""
from typing import List


class Solution:
    # Runtime: 77ms
    # Memory Usage: 49MB
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        before = intervals[0]
        count = 0
        for i in range(1, len(intervals)):
            current = intervals[i]
            if current[0] < before[1]:
                count += 1
            else:
                before = current
        return count

    # Best time complexity solution (1ms)
    def eraseOverlapIntervalsBestTime(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        prev = - float ('inf'); keep = 0
        for item in intervals:
            if item[0]>=prev:
                prev = item[1]
                keep +=1
        return len(intervals) - keep

    # Best memory complexity solution (37.6MB)
    def eraseOverlapIntervalsBestMemory(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x:x[1])
        num_rem = 0
        end = intervals[0][1]
        for i in intervals[1:]:
            cur_start = i[0]
            if cur_start < end:
                intervals.remove(i)
                num_rem+=1
            else:
                end=i[1]
        return num_rem


if __name__ == "__main__":
    s = Solution()

    print(s.eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]])) # 1
    print(s.eraseOverlapIntervals([[1,2],[1,2],[1,2]])) # 2
    print(s.eraseOverlapIntervals([[1,2],[2,3]])) # 0
