# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findMin(self, root: TreeNode) -> TreeNode:
        
        while root and root.left:
            root = root.left
        
        return root
        

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:

        if not root:
            return None

        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            # If node have 0 or 1 child:
            if not root.right:
                return root.left
            elif not root.left:
                return root.right

            # If node have 2 child:
            else:
                min_node = self.findMin(root.right)
                root.val = min_node.val
                root.right = self.deleteNode(root.right, min_node.val)

        return root
