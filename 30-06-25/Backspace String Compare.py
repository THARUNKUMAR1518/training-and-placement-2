class Solution(object):
    def backspaceCompare(self, s, t):
        def process_string(s):
            stack = []  
            for char in s:
                if char != '#':
                    stack.append(char)  
                elif stack:
                    stack.pop() 
            return ''.join(stack)  

        processed_S = process_string(s)
        processed_T = process_string(t)

        return processed_S == processed_T
