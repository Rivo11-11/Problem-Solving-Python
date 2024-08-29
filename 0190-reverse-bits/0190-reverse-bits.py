class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):

        def convert_binary(dec) :
            res = ''
            while dec :
                if dec % 2 == 0 :
                    res += '0'
                else :
                    res += '1'
                dec //= 2
            length = len(res) 
            while length < 32 :
                res += '0'
                length +=1
            return res
        def convert_dec(bin) :
            length  = len(bin) 
            sum = 0
            j = length - 1
            for i in range(length) :
                if bin[i] == '1' :
                    sum += 2**j
                j-=1
            return sum

        bin = convert_binary(n)
        return convert_dec(bin)