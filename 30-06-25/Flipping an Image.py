class Solution(object):
    def flipAndInvertImage(self, image):
        n = len(image)
        for i in range(n):
            for j in range((n + 1) // 2):
                temp = image[i][j]
                image[i][j] = image[i][n - j - 1] ^ 1
                image[i][n - j - 1] = temp ^ 1
                
        return image
