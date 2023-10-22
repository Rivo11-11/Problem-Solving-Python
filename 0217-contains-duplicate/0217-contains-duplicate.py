class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
          # Solution 1:
        # i = 0 
        # j = 0 
        # for i in range(len(nums)):
        #   for j in range(i+1,len(nums)):
        #         if nums[i] == nums[j]:
        #          return True
        # return False
      # Solution 2:
        # hashset=set()
        # for n in nums:
        #   if n in hashset:
        #     return True 
        #   hashset.add(n)
        # return False
      # Solution 3
       ## Sort and compare adjacent
        nums.sort()
        for i in range(len(nums)):
         if i != len(nums)-1:
          if nums[i]==nums[i+1]:
            return True
        return False
        