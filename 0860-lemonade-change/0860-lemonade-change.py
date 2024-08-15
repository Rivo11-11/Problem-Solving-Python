class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        n = len(bills)
        mymap = defaultdict(int)
        for i in range(n) :
            if bills[i] == 10 :
                if not mymap[5] : return False 
                mymap[5] -= 1
                
            if bills[i] == 20 :
                if not (mymap[5] and mymap[10]) and mymap[5] < 3 : return False 
                if mymap[10] :
                    mymap[10] -= 1
                    mymap[5] -= 1
                else :
                    mymap[5] -= 3
            mymap[bills[i]] += 1 
        return True
