class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        l, r, m = 0, len(nums)-1, 0

        while l <= r:
            m = (l + r) // 2
            if nums[m] > nums[r]:
                l = m + 1
            elif nums[m] < nums[r]:
                r = m
            else:
                return nums[m]
                
        return nums[m]    
