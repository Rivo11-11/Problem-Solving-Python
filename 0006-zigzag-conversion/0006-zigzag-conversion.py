class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 :
            return s
        lists = [[] for _ in range(numRows)]
        counter = 0
        flag =True
        for i in range(len(s)) : 
            lists[counter].append(s[i])
            if flag :
             counter += 1
            else : 
             counter -= 1
            if counter == numRows - 1 :
                flag = False
            if counter == 0 :
                flag =True
                
        combined_string = ""
        for sublist in lists:
            for item in sublist:
                combined_string += item
        return combined_string
     