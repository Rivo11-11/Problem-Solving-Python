class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        maxi = max(piles)
        n = len(piles)
        l,r = 1,maxi 
        mini = float('inf')
        while l <= r :
            mid =  (l + r) // 2 
            finish = 0
            for pile in piles :
                finish += math.ceil(pile*1.0 / mid)
            if finish == h :
                mini = min(mini,mid)
                r = mid - 1
            ## i need to each faster
            elif finish > h : 
                l = mid + 1
            
            ## i need to eat slower but save the answer it could be the answer within 1 hour
            else : 
                mini = min(mini,mid)
                r = mid - 1
        return mini
