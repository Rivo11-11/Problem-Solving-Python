class Solution(object):
    def eliminateMaximum(self, dist, speed):
        """
        :type dist: List[int]
        :type speed: List[int]
        :rtype: int
        """
        ## insertion sort
        n = len(dist)
        time = []
        for i in range(n) :
            div = math.ceil((dist[i]*1.0 / speed[i]))
            if div == 0 : div = 1
            time.append(div) 

        time.sort()
        count = 0
        for i in range(n) :
            if time[i]-i > 0 :
                count += 1
            else :
                break
        return count
            


        