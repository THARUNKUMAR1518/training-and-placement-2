class Solution(object):
    def commonChars(self, words):
        res = []
        for ch in set(words[0]):
            res += ch * min([word.count(ch) for word in words]) 
        return res
