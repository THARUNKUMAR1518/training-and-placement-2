class Solution(object):
    def sortArrayByParityII(self, A):
        i, j, L = 0, 1, len(A)              
        while j < L:                        
            if A[j] % 2 == 0:             
                A[j], A[i] = A[i], A[j]     
                i += 2                       
            else:
                j += 2
        return A
