class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        num_set = set(nums)

        for num in num_set:
            if num - 1 not in num_set:
                i = 1
                while num + i in num_set:
                    i += 1
                res = max(i, res)

        return res
