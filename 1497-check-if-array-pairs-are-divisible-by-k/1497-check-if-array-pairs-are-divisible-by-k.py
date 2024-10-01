class Solution(object):
    def canArrange(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: bool
        """
        k_list = [0 for i in range(k)]
        for e in arr :
            k_list[e%k] += 1
        l,r = 1,k-1 
        ## number that can be divided by k are odd then false
        if k_list[0] % 2 != 0 :
            return False 
        while l < r :
            if k_list[r] != k_list[l] :
                return False
            r -= 1 
            l += 1
        return True

        
        