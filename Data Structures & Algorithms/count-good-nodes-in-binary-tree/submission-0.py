# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count_good = 0

        tree_stack = [root]
        min_stack = [root.val]

        while len(tree_stack) > 0:
            tree_node = tree_stack.pop(-1)
            min_value = min_stack.pop(-1)

            if tree_node is None:
                continue
            
            if tree_node.val >= min_value:
                count_good += 1
        
            tree_stack.append(tree_node.left)
            min_stack.append(max(tree_node.val, min_value))

            tree_stack.append(tree_node.right)
            min_stack.append(max(tree_node.val, min_value))

        return count_good