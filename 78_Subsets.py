class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        subset = []

        def dfs(i):
            if i >= len(nums):
                ans.append(subset[:])
                return 

            subset.append(nums[i])
            dfs(i + 1)

            subset.pop()
            dfs(i + 1)

        dfs(0)
        return ans
            
        
