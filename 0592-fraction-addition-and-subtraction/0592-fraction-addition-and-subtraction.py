from fractions import Fraction
class Solution(object):
    def fractionAddition(self, expression):
        """
        :type expression: str
        :rtype: str
        """
        numbers = []
        n = len(expression)
        s = 0
        end_fraction = 0
        flag_negative = False
        prev = None
        for i, chr in enumerate(expression): 
            if chr == '-' :
                flag_negative = True
                continue 
            if chr.isnumeric() :
                if prev :
                    prev = False
                    continue
                new_char = chr
                if i < n-1 and expression[i+1].isnumeric() :
                  new_char = chr + expression[i+1]
                  prev = True
                numbers.append(int(new_char))
                end_fraction += 1
            if end_fraction == 2 :

                if flag_negative :
                    s -= numbers[0]*1.0 / numbers[1] 
                else :
                    s += numbers[0]*1.0 / numbers[1] 
                end_fraction = 0 
                numbers = []
                flag_negative = False 
        s_fraction = Fraction(s).limit_denominator()
        if s_fraction == int(s_fraction) :
            return str(s_fraction) + '/' + '1'
        return str(s_fraction)


            