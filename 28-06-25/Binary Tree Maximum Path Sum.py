class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.max = float('-inf')
        self.RecursiveMaxPathSum(root)

        return self.max

    def RecursiveMaxPathSum(self, node):
        if not node:
            return 0
        
        left = self.RecursiveMaxPathSum(node.left)
        right = self.RecursiveMaxPathSum(node.right)

        left = left if left > 0 else 0
        right = right if right > 0 else 0

        CurrentSum = right + left + node.val
        self.max = max(self.max, CurrentSum)

        return CurrentSum - min(left, right)
