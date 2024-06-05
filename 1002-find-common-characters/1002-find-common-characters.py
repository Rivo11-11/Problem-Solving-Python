class Solution(object):
    def commonChars(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        n = len(words)
        mylist = []
        i = 0
        for word in words :
            mymap = {}
            for s in word :
                if s in mymap :
                    mymap[s] += 1
                else : mymap[s] = 1
            mylist.append(mymap)
        ref = mylist[0]
        for mapp in mylist :
            for key,val in ref.items() :
                if key not in mapp :
                    ref.pop(key)
                else :
                    ref[key] = min(val,mapp[key])
        res = []
        for key,val in ref.items() :
            for i in range(val) :
                res.append(key)
        return res

