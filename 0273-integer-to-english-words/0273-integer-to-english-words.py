class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        mymap = {
        0 : "Zero",
        1: "One",
        2: "Two",
        3: "Three",
        4: "Four",
        5: "Five",
        6: "Six",
        7: "Seven",
        8: "Eight",
        9: "Nine",
        10: "Ten",
        11: "Eleven",
        12: "Twelve",
        13: "Thirteen",
        14: "Fourteen",
        15: "Fifteen",
        16: "Sixteen",
        17: "Seventeen",
        18: "Eighteen",
        19: "Nineteen",
        20: "Twenty",
        30: "Thirty",
        40: "Forty",
        50: "Fifty",
        60: "Sixty",
        70: "Seventy",
        80: "Eighty",
        90: "Ninety",
        100: "Hundred",
        1000 : "Thousand",
        1000000 : "Million",
        1000000000 : "Billion"
        }

        ## base case if number exist in my dictionary
        if num in mymap :
            if num > 90 :
                return "One " + mymap[num] 
            return mymap[num]

        n = 0
        d = defaultdict(str)
        key = 0

        ## group each 3 number together
        for c in reversed(str(num)) :
            if n and n % 3 == 0 : 
                key += 1
            d[key] += c
            n+=1

        ## convert from 000 to 999
        def rec(n,curr,s) :
                if n == 0 :
                    ## i don't want to return 'Zero' if the last character was 0
                    if s[n] == '0' : return curr
                    return curr + ' ' + mymap[int(s[n])]

                ## skip if u found a zero
                if s[n] == '0' :
                    return rec(n-1,curr,s)
                
                ## special 2 digit number first digit is 1 or second is 0
                if n == 1 and (s[1] == '1' or s[0] == '0'):
                    return curr + ' ' + mymap[int(s[1] + s[0])]
                
                ## non special 2 digit number ex : 34 
                if n == 1 :
                     return rec(n-1,curr + ' ' + mymap[int(s[n]) * 10**n],s)

                ## 3 digit number
                if n == 2 :
                    return rec(n-1,curr + ' ' + mymap[int(s[n])] + ' '+ mymap[10**n],s)
    

        res = ''
        # pass the partitioned number to the rec converter
        while key > -1 :
            temp = rec(len(d[key])-1,'',d[key])
            ## i got a 000 don't added a suffix
            if not temp :
                key-=1
                continue
            res += temp + ' '
            if key == 3  :
                res += 'Billion'
            elif key == 2 :
                res += "Million"
            elif key == 1 :
                res += "Thousand"
            key -=1
        
        ## remove additive start and end spaces (trim function)
        return res.strip()

        