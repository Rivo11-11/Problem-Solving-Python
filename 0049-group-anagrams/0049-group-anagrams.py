class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        mymap = defaultdict(list)
        for word in strs :
            s = sorted(word)
            s = ''.join(s)
            mymap[s].append(word) 
          
        res = []
        for k,v in mymap.items() :
         res.append(v)
        return res