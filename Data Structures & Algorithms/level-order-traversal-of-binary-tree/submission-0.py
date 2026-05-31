# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        order = []

        root_stack = [root]
        depth_stack = [0]

        while len(root_stack) > 0:
            
            root_node = root_stack.pop(-1)
            depth_node = depth_stack.pop(-1)

            if root_node is None:
                continue

            if len(order) <= depth_node:
                order.append([])
            order[depth_node].append(root_node.val)

            root_stack.append(root_node.right)
            depth_stack.append(depth_node + 1)
            root_stack.append(root_node.left)
            depth_stack.append(depth_node + 1)

        return order