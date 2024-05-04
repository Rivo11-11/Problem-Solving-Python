class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        people.sort()
        n = len(people)
        l = 0 
        r = n - 1 
        count = 0
        while l < r :
            if people[l] + people[r] > limit : 
                count += 1 
                r -= 1
            elif people[l] + people[r] <= limit : 
                count += 1 
                r-=1 
                l+=1
            
        ## odd case
        if l == r :
            count += 1
        return count


        
        