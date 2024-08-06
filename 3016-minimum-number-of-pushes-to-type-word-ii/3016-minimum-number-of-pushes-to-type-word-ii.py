class Solution(object):
    def minimumPushes(self, word):
        """
        :type word: str
        :rtype: int
        """
        mymap = defaultdict(int) 
        for c in word :
            mymap[c] += 1 
        vals = mymap.values()
        vals.sort()
        total = 0
        factor = 1
        index = 1
        for val in reversed(vals):
            total += val * factor
            ## each 8 step increase the factor by 1
            if index % 8 == 0: 
                factor += 1
            index += 1
        return total


        
        