class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        start = 0
        finish = n - 1

        def binary_search_recursive(start, finish):
         if start > finish:
            return -1

         mid = start + (finish - start) // 2

         if nums[mid] == target:
            return mid
         elif nums[mid] > target:
            return binary_search_recursive(start, mid - 1)
         else:
            return binary_search_recursive(mid + 1, finish)

        return binary_search_recursive(start,finish)
        