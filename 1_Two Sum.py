class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        pair = {}

        for i in range (len(nums)):
            diff = target - nums[i]
            if diff in pair:
                return [pair[diff], i]
            else:
                pair[nums[i]] = i

        return -1
