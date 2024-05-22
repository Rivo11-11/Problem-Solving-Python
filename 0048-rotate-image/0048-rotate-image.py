class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix) 
        l,r = 0 , n - 1 
        while l < r :
            top,bottom = l,r 
            for i in range(r-l) :
                topLeft = matrix[top][l+i] 
                matrix[top][l+i] = matrix[bottom - i][l]
                matrix[bottom-i][l] = matrix[bottom][r-i]
                matrix[bottom][r-i] = matrix[top+i][r] 
                matrix[top+i][r] = topLeft
            l += 1 
            r -=1 
                

        