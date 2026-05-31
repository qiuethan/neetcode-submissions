# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        p_ancestors = []
        q_ancestors = []

        def find_p(root):
            nonlocal p

            if root is None:
                return False
            
            if root.val == p.val:
                p_ancestors.append(root)
                return True
            
            if find_p(root.left):
                p_ancestors.append(root)
                return True
            if find_p(root.right):
                p_ancestors.append(root)
                return True
        
        def find_q(root):
            nonlocal q

            if root is None:
                return False
            
            if root.val == q.val:
                q_ancestors.append(root)
                return True
            
            if find_q(root.left):
                q_ancestors.append(root)
                return True
            if find_q(root.right):
                q_ancestors.append(root)
                return True
        
        find_p(root)
        find_q(root)

        p_ancestors.reverse()
        q_ancestors.reverse()

        print([p_ancestor.val for p_ancestor in p_ancestors], [q_ancestor.val for q_ancestor in q_ancestors])

        for i in range(min(len(p_ancestors), len(q_ancestors))):
            if p_ancestors[i].val != q_ancestors[i].val:
                return p_ancestors[i-1]
        
        if len(p_ancestors) < len(q_ancestors):
            return p_ancestors[-1]
        else:
            return q_ancestors[-1]
