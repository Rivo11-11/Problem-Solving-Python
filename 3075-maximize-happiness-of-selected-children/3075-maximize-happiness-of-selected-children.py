class Solution(object):
    def maximumHappinessSum(self, happiness, k):
        """
        :type happiness: List[int]
        :type k: int
        :rtype: int
        """
        happiness.sort(reverse = True) 
        s = 0
        dec = 0
        for i in range(k) :
            if happiness[i] - dec > 0 : s+=happiness[i]-dec
            else :
                break
            dec += 1
        return s

        