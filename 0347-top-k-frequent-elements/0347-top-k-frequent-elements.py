class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        n = len(nums)
        mymap = defaultdict(int)
        maxi = 0
        for i in range(n) :
            mymap[nums[i]] += 1
            maxi = max(maxi,mymap[nums[i]])
        new_map =defaultdict(list)
        for key,v in mymap.items() :
            new_map[v].append(key)
        res = []
        # print(new_map)
        for i in reversed(range(1,maxi+1)) :
            if k :
                res.extend(new_map[i])
                k-=len(new_map[i])
            else :
                break 
        return res

