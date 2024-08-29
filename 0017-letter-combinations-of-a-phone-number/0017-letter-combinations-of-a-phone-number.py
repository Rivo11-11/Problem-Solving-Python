class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits :
            return []
        n = len(digits)
        mymap = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz"
        }

        res = []
        def backtrack(s,string) :
            if s == n :
                print('a7aaa')
                res.append(string)
                return 
            digit = digits[s]
            for i in range(len(mymap[digit])) :
                backtrack(s+1,string + mymap[digit][i])
        backtrack(0,'')
        return res
 
        