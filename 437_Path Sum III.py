# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        # DFS + PrefixSum approach
        res = 0
        sum_map = {0: 1}

        def dfs(root, total):
            nonlocal res
            if not root:
                return

            total += root.val

            res += sum_map.get(total-targetSum, 0)
            sum_map[total] = sum_map.get(total, 0) + 1

            dfs(root.left, total)
            dfs(root.right, total)
            sum_map[total] -= 1

        dfs(root, 0)

        return res
            
