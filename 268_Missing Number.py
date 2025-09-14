class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        length = 0
        total = 0

        for i in range(len(nums)):
            length += i + 1
            total += nums[i]

        return length - total
