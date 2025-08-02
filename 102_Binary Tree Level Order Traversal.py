# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Append root

        ans = []
        
        def BST(root):

            queue = deque()

            if root:
                queue.append(root)

            while queue:
                # FIFO
                level =  []
                for i in range(len(queue)):
                    
                    curr = queue.popleft()
                    level.append(curr.val)

                    if curr.left:
                        queue.append(curr.left)
                    if curr.right:
                        queue.append(curr.right)

                ans.append(level)
        
        BST(root)

        return ans
