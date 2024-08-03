from typing import List


# Solution 1
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(2):
            for n in nums:
                ans.append(n)
        return ans

# Solution 2
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # copy values, otherwise both ans and nums will have same memory address (cause infinite loops)
        ans = nums.copy()
        for num in nums:
            ans.append(num)
        return ans

# Solution 3
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        size = len(nums)
        for i in range(size):
            nums.append(nums[i])
        return nums
