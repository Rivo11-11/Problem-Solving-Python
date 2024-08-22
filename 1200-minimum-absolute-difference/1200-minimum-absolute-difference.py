class Solution(object):
    def minimumAbsDifference(self, arr):
        """
        :type arr: List[int]
        :rtype: List[List[int]]
        """
        arr.sort()
        n = len(arr)
        mini = float('inf')
        result = []
        for i in range(n-1) :
            if arr[i+1] - arr[i] < mini :
                mini = arr[i+1] - arr[i]
                result = []
            if arr[i+1] - arr[i] > mini :
                continue
            result.append([arr[i],arr[i+1]]) 
        return result



        