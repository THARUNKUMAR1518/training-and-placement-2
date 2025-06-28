class Solution(object):
    def increasingBST(self, root):
        if not root:
            return None
        stack = []
        temp = x = root
        i = 0
        while stack or temp:
            if temp:
                stack.append(temp)
                temp = temp.left
            else:
                node = stack.pop()
                if i==0:
                    root = x = node
                    i+=1
                else:
                    x.right = node
                    x = node
                    x.left = None
                temp = node.right
        return root	
		
