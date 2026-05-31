# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        max_depth = 1

        q = []
        depth = []

        q.append(root)
        depth.append(1)

        while len(q) > 0:
            node = q.pop(-1)
            node_depth = depth.pop(-1)

            max_depth = max(max_depth, node_depth)

            if node.left is not None:
                q.append(node.left)
                depth.append(node_depth + 1)
            if node.right is not None:
                q.append(node.right)
                depth.append(node_depth + 1)
        
        return max_depth