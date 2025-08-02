# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        def inorder(root, k):
        # In order BST traverse
            if not root:
                return

            inorder(root.left, k)
            ans.append(root.val)
            inorder(root.right, k)

        ans = []
        inorder(root, k)
        
        return ans[k - 1]

