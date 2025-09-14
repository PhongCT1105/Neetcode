class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(curr, left):
            if not left:
                res.append(curr[:]) 
                return

            for i in range(len(left)):
                pick = left[i]
                print(curr)
                dfs(curr + [pick], left[:i] + left[i+1:])
                
        dfs([], nums)
        return res
