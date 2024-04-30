class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        A,B = nums1 , nums2
        total = len(A) + len(B) 
        half = total // 2 
        if len(A) > len(B) : 
            A,B = B,A 
        ## Binary Search on the smaller list
        m = len(A) 
        n = len(B)
        l = 0 
        r = m - 1
        while True : 
            mid_A = (l+r) // 2 
            mid_B = half - mid_A - 2
            Aleft = A[mid_A] if mid_A >= 0 else float('-inf')
            Aright = A[mid_A + 1] if mid_A + 1 < m  else float('inf')
            Bleft = B[mid_B] if mid_B >= 0 else float('-inf')
            Bright = B[mid_B + 1] if mid_B + 1 < n else float('inf')
            ## i found the left side correctly
            if Bright >= Aleft and Aright >= Bleft : 
                ## odd case 
                if total % 2 != 0 :
                    return min(Aright,Bright) 
                ## even case
                else : 
                    return (max(Aleft,Bleft) + min(Aright,Bright)) / 2.0
            elif Bright < Aleft : 
                r = mid_A - 1 
            else : 
                l = mid_A + 1





        