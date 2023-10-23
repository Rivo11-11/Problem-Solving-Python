class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
         ## Sol 1:
        # mylist=list()
        # if len(s) == len(t):
        #     for n in s:
        #         mylist.append(n)
        #     for n in t:
        #         if n not in mylist:
        #             return False
        #         else :
        #             mylist.remove(n)
        #     return True
        # return False
     ## Sol: 2
        # if len(s) == len(t):
        #  lst1 = list(s)
        #  lst2 = list(t)
        #  lst1.sort()
        #  lst2.sort()
        #  if lst1==lst2 :
        #   return True 
        #  else :
        #   return False
        # return False
     ## Sol 3:
        map1 = {}
        map2= {}
        if len(s) == len(t):
            for letter in s:
               if letter in map1:
                 map1[letter] += 1
               else:
                  map1[letter] = 1
            for letter in t:
               if letter in map2:
                  map2[letter] += 1
               else:
                  map2[letter] = 1
            for key, value in map1.items():
                if key in map2 and map2[key] == value:
                  continue
                else:
                  return False
            return True
            
        return False
        