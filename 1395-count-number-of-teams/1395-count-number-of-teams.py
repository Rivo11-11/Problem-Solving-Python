class Solution(object):
    def numTeams(self, rating):
        """
        :type rating: List[int]
        :rtype: int
        """
        ## think about the middle approach
        ## loop on each element consider it the middle 
        n = len(rating) 
        count = 0
        for i in range(n) :
            next_count = 0
            prev_count = 0
            for j in range(n) :
                if rating[i] < rating[j] and i < j :
                    next_count += 1 
                elif rating[i] > rating[j] and i > j :
                    prev_count += 1 
            ## calculate the ascending order 
            count += next_count * prev_count
            ## formula to calculate the descending order
            count += (n-1-i-next_count) * (i-prev_count)
        

        return count
