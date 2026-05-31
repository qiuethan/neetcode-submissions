# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    treeSizeMemo = {}

    def treeSize(self, root) -> int:

        if root is None:
            return 0

        if root.val in self.treeSizeMemo:
            return self.treeSizeMemo[root.val]
        
        self.treeSizeMemo[root.val] = 1 + self.treeSize(root.left) + self.treeSize(root.right)

        return self.treeSizeMemo[root.val]
    
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        self.treeSizeMemo = {}

        return self.kthSmallestRecursion(root, k)

    def kthSmallestRecursion(self, root: Optional[TreeNode], k: int) -> int:

        if self.treeSize(root.left) == k - 1:
            return root.val

        if self.treeSize(root.left) > k - 1:
            return self.kthSmallestRecursion(root.left, k)
        
        return self.kthSmallestRecursion(root.right, k - 1 - self.treeSize(root.left))