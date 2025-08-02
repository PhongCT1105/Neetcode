# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        ans = []

        def BST(root):

            queue = deque()
            if root:
                queue.append(root)

            while queue:
                level = []
                for _ in range(len(queue)):
                    curr = queue.popleft()
                    level.append(curr.val)

                    if curr.left:
                        queue.append(curr.left)
                    if curr.right:
                        queue.append(curr.right)

                if level:
                    ans.append(level[-1])

        BST(root)
        return ans
