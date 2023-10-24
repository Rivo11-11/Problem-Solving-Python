class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result=[]
        n=len(nums)
        nums.sort()
        for i in range(n-2):
          if i>0 and nums[i]==nums[i-1]:
              continue
          r=n-1
          l=i+1
          while r>l:
             if nums[i]+nums[l]+nums[r]==0:
                 result.append([nums[i],nums[l],nums[r]])
                 l+=1
                 while nums[l]==nums[l-1] and l < r:
                   l+=1
             elif nums[l]+nums[r]+nums[i]>0:
                r-=1
             else:
                l+=1
        return result

        