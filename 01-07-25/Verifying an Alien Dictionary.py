class Solution(object):
    def isAlienSorted(self, words, order):
        orderRange_inDictionary = {char:i for i,char in enumerate(order)}
        sizeWords=range(len(words)-1)

        def compared_words(word1, word2):
            smallerChar=True
            biggerChar=False
            size_word1=len(word1)
            size_word2=len(word2)
            
            for char1, char2 in zip(word1, word2):
                if orderRange_inDictionary[char1] < orderRange_inDictionary[char2]:
                    return smallerChar
                elif orderRange_inDictionary[char2] < orderRange_inDictionary[char1]:
                    return biggerChar 
            return size_word1 <= size_word2
        
        
        return all(compared_words(words[i],words[i+1]) for i in sizeWords)
