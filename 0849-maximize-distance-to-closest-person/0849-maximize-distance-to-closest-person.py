class Solution(object):
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        ## get maximum conecutive zero
        count_0 = 0
        start_0 = 0
        maxi = 0
        n = len(seats)
        flag = True
        for i in range(n) :
            ## get the start consecutive zeros 
            if seats[i] == 0 and flag :
                start_0 +=1
            else :
                flag = False
            ## get max consecutives zero and also the end consecitive zeros
            if seats[i] == 0 :
                count_0 += 1
                maxi = max(maxi,count_0)
            else :
                count_0 = 0 
        return max(int(math.ceil(maxi/2.0)),start_0,count_0)


