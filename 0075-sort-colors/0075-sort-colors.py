class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        mymap = {
            0 : 0,
            1 : 0, 
            2 : 0
        }
        n = len(nums)
        for i in range(n) :
             mymap[nums[i]] += 1
        i = 0
        for j in range(3) :
            while mymap[j] :
                nums[i] = j 
                i += 1
                mymap[j] -= 1
               
            
         
       
            

        