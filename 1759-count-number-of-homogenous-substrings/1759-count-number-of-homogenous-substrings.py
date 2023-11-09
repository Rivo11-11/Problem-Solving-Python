class Solution(object):
    def countHomogenous(self, s):
        """
        :type s: str
        :rtype: int
        """
        mymap  = {}
        i = 0
        while i < len(s) :
          string = ""
          string+=s[i]
          new = i + 1
          while  new < len(s) and s[new] == s[i] :
              string +=s[new]
              new+=1
          if string not in mymap :
              mymap[string] = 1
          else :
              mymap[string]+=1
          i=new
        mysum = 0
        for key,value in mymap.items() :
            n = len(key)
            mysum += (n * (n+1) * value )/ 2
        return mysum % (10**9 + 7)




        