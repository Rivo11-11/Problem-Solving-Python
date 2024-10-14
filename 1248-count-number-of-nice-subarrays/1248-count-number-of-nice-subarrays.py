class Solution(object):
    def numberOfSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        mymap = defaultdict(int)
        mymap[0] += 1
        n,pre,count = len(nums),0,0
        for i in range(n) :
            if nums[i] % 2 == 1 :
                nums[i] = 1 
            else :
                nums[i] = 0
            nums[i] += pre 
            pre = nums[i]
            mymap[pre] += 1 
        for i in range(n) :
            if nums[i]-k in mymap :
                count += mymap[nums[i]-k]
                
        return count 

