# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        tree_stack = [root]
        bounds = [(-1001, 1001)]

        while len(tree_stack) > 0:
            tree_node = tree_stack.pop(-1)
            bound = bounds.pop(-1)
            
            if tree_node is None:
                continue
            
            if tree_node.left is not None:
                if bound[0] < tree_node.left.val and tree_node.left.val < bound[1] and tree_node.left.val < tree_node.val :
                    tree_stack.append(tree_node.left)
                    bounds.append((bound[0], tree_node.val))
                else:
                    return False

            if tree_node.right is not None:
                if bound[0] < tree_node.right.val and tree_node.right.val < bound[1] and tree_node.right.val > tree_node.val:
                    tree_stack.append(tree_node.right)
                    bounds.append((tree_node.val, bound[1]))
                else:
                    return False
        

        return True
