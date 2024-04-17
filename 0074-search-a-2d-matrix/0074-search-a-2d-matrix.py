class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        # m = len(matrix) ## row
        # n = len(matrix[0]) ## col 
        # for i in range(m) :
        #     l = 0
        #     r = n - 1 
        #     while l <= r : 
        #         mid = (l+r) // 2 
        #         if matrix[i][mid] == target :
        #             return True 
        #         elif matrix[i][mid] < target : 
        #             l = mid + 1 
        #         else : 
        #             r = mid - 1
        # return False 
 
        ## Optimize o(lgm + lgn)
        # m = len(matrix) ## row
        # n = len(matrix[0]) ## col 
        # top = 0
        # bottom = m - 1
        # middle = 0
        # while top <= bottom : 
        #     middle = (top + bottom) // 2
        #     if matrix[middle][0] <= target and target <= matrix[middle][n-1] :
        #         break 
        #     elif matrix[middle][n-1] <  target : 
        #         top = middle + 1
        #     else :
        #         bottom = middle - 1 
        
        # l = 0 
        # r = n - 1 
        # while l <= r : 
        #     mid = (l+r) // 2 
        #     if matrix[middle][mid] == target : return True 
        #     elif matrix[middle][mid] > target :
        #         r = mid - 1
        #     else : 
        #         l = mid + 1 
        # return False 

        ## O(lg(m*n))...2d => 1d .. m*n 
        m, n = len(matrix), len(matrix[0])
        first, last = 0, m * n - 1
        while last >= first:
            index_mid = (first + last) // 2
            row = index_mid // n 
            col = index_mid % n 
            if  matrix[row][col] == target:
                return True
            elif  matrix[row][col] < target:
                first = index_mid + 1
            else:
                last = index_mid - 1
        return False

      






















       