class Solution(object):
    def findRotation(self, mat, target):
        """
        :type mat: List[List[int]]
        :type target: List[List[int]]
        :rtype: bool
        """
        def rotate(matrix,n) :
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
        n = len(mat)
        for k in range(4) :
            flag = True
            for i in range(n) :
                for j in range(n) :
                    if mat[i][j] != target[j][n-1-i] :
                        flag = False
                        break 
                if not flag :
                    break
            if flag :
                return True
            rotate(mat,n)
        return False
                    

        
        