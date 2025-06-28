class Solution(object):
    def isCousins(self, root, x, y):
        q = collections.deque()
        q.append([root, root])
        while q:
            level = {}
            for _ in range(len(q)):
                node = q.popleft()
                child = node[0]
                parent = node[1]
                level[child.val] = parent.val
                if child.left:
                    q.append([child.left, child])
                if child.right:
                    q.append([child.right, child])
                    
            if (x in level) ^ (y in level):
                return False
            
            if x in level and y in level:
                if level[x] == level[y]:
                    return False
                return True
            
        return False
		
