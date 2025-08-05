class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        ans = []

        def dfs(i, subset, sum):

            if sum == target:
                ans.append(subset[:])
                return 
            
            if i >= len(candidates) or sum > target:
                return 

            subset.append(candidates[i])
            sum += candidates[i]

            dfs(i, subset, sum)
            subset.pop()

            sum -= candidates[i]
            dfs(i + 1, subset, sum)

        dfs(0, [], 0)
 
        return ans
