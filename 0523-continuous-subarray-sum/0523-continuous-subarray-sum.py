class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        ## always exist
        mymap = {}
        mymap[0] = -1
        if nums[0] % k != 0 :
         mymap[nums[0]%k] = 0 
        n = len(nums)
        for i in range(1,n) :
            nums[i] += nums[i-1] 
            ## check if that modulus encountred before and check if it not the previous element to not form a subarray of 1 element 
            mod =  nums[i] % k
            if mod in mymap and mymap[mod] != i-1 :
                return True
            if mod not in mymap :
                mymap[mod] = i   
        return False