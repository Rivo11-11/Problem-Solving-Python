class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        def convert_to_binary(num) :
            stack = [] 
            while num : 
                if num % 2 == 0 : 
                    stack.append('0') 
                else :
                    stack.append('1')
                num/=2
            return ''.join(stack)
        
        def convert_to_decimal(bin) :
            num = 0
            pow = 0
            for c in bin :
                if c == '1' :
                    num += 2**pow 
                pow += 1
            return num
        
        def complement(bin) :
            str = ''
            for c in bin :
                if c == '1' :
                    str += '0'
                else :
                    str += '1'
            return str
                
        bin = convert_to_binary(num)
        bin = complement(bin) 
        return convert_to_decimal(bin)

        