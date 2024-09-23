class Solution(object):
    def convertDateToBinary(self, date):
        """
        :type date: str
        :rtype: str
        """
        def convert_to_binary(n) :
            string = ''
            while n :
                if n % 2 :
                    string += '1'
                
                else : 
                    string += '0'

                n //=2
            return string
        
        date_list = date.split('-') 
        res = ''
        n = len(date_list)
        for i in range(n) :
            res += convert_to_binary(int(date_list[i]))[::-1]
            if i != n-1 : res += '-'

        return res
    