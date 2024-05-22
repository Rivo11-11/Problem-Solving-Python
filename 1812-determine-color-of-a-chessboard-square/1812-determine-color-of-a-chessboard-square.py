class Solution(object):
    def squareIsWhite(self, coordinates):
        """
        :type coordinates: str
        :rtype: bool
        """
        ## odd - odd => False 
        ## even - odd => True
        mymap = {}
        s = ord('a')
        for i in range(8) : 
            mymap[chr(s)] = i+1
            s+=1
        data = list(coordinates)
        row = mymap[data[0]]
        col = int(data[1])
        if row % 2 != 0 :
            if col % 2 != 0 :
                return False 
            return True 
        if row % 2 == 0 :
            if col % 2  != 0 :
                return True
            return False
        