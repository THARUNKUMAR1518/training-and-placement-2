class Solution(object):
    def leafSimilar(self, root1, root2):
        self.ans1=[]
        self.ans2=[]
        def traversal1(root):
            if root==None:
                return
            traversal1(root.left)
            traversal1(root.right)
            if root.left==None and root.right==None:
                self.ans1.append(root.val)
        def traversal2(root):
            if root==None:
                return
            traversal2(root.left)
            traversal2(root.right)
            if root.left==None and root.right==None:
                self.ans2.append(root.val)
        traversal1(root1)
        traversal2(root2)
        if len(self.ans1)!=len(self.ans2):
            return False
        for i in range(len(self.ans1)):
            if self.ans1[i]!=self.ans2[i]:
                return False
        return True


        
