class Solution(object):
    def isUnivalTree(self, root):
        self.value = root.val
        
        def dfs(root):
            if root:
                if self.value != root.val:
                    return False
                return dfs(root.left) and dfs(root.right)
            return True
        return dfs(root)
