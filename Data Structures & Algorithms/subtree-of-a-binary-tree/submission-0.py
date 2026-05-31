# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
    
        def isSameTree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
            p_stack = []
            q_stack = []

            p_stack.append(p)
            q_stack.append(q)

            while len(p_stack) > 0:
                p_root = p_stack.pop(-1)
                q_root = q_stack.pop(-1)

                if p_root is None and q_root is not None:
                    return False
                if p_root is not None and q_root is None:
                    return False

                if p_root is not None and q_root is not None:
                    
                    if p_root.val != q_root.val:
                        return False

                    p_stack.append(p_root.left)
                    q_stack.append(q_root.left)
                    p_stack.append(p_root.right)
                    q_stack.append(q_root.right)
            
            return True
        
        tree_stack = [root]

        while len(tree_stack) > 0:
            tree_root = tree_stack.pop(-1)
            if tree_root is None:
                continue

            if isSameTree(tree_root, subRoot):
                return True
            
            tree_stack.append(tree_root.left)
            tree_stack.append(tree_root.right)
        
        return False