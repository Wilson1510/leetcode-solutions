"""
Complexity:
- Time  : O(n)
- Space : O(1)
"""
from typing import List

class Solution:
    # Runtime: 0ms
    # Memory Usage: 19.38MB
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        k = 0

        for i in range(n):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k

    # Best time complexity solution (0ms)
    def removeElementBestTime(self, nums: List[int], val: int) -> int:
        import logging

        invalid_indexes = set()
        for i in range(len(nums)):
            if nums[i] == val:
                invalid_indexes.add(i)
        
        logging.info('invalid_indexes=%s', invalid_indexes)

        value_index = 0
        for i in range(len(nums)):
            if i in invalid_indexes:
                continue
            else:
                logging.info("adding %s", nums[i])
                nums[value_index] = nums[i]
                value_index += 1
        
        return value_index

    # Best memory complexity solution (16.6MB)
    def removeElementBestMemory(self, nums: List[int], val: int) -> int:
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        
        return k


if __name__ == "__main__":
    s = Solution()

    print(s.removeElement([3,2,2,3], 3)) # 2, nums = [2,2,_,_]
    print(s.removeElement([0,1,2,2,3,0,4,2], 2)) # 5, nums = [0,1,4,0,3,_,_,_]
