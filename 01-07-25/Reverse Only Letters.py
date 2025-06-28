class Solution(object):
    def reverseOnlyLetters(self, s):
        chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
        s = list(s)
        i = 0
        j = len(s) - 1

        while (i < j) :
            if s[i] not in chars:
                i += 1
            elif s[j] not in chars:
                j -= 1
            
            else :
                s[i] , s[j] = s[j] , s[i]
                i += 1
                j -= 1

        return "".join(s)
