class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        nums.sort() 
        n = len(nums)
        res = [0 for i in range(n)] 
        mid = n // 2
  
        if n%2 == 1 :
           mid += 1
  
        l = 0
        r = 0
        stack1 = []
        stack2 = []
        for i in range(n) :
            if i < mid : 
              stack1.append(nums[i]) 
              l+=1
            else :
              stack2.append(nums[i])
              r+=1
        s = 0
        e = 1
        for i in range(l) :
            nums[s] = stack1.pop()
            s+=2 
        for i in range(r) :
            nums[e] = stack2.pop()
            e+=2
        





        