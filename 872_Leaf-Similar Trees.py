# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if not root1 or not root2:
            return false
        
        arr = []
        def get_leaf(root):
            
            if not root.left and not root.right:
                nonlocal arr
                arr.append(root.val)

            if root.left:
                get_leaf(root.left)
            if root.right:
                get_leaf(root.right)

        get_leaf(root1)
        arr1 = arr[:]
        arr = []
        get_leaf(root2)

        return arr1 == arr
