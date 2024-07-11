class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        n = len(candidates)
        res = []
        candidates.sort()
        def backtrack(s,tracker,tot) :
            if tot > target :
                return
            if tot == target :
                res.append(tracker[:])
                return
            for i in range(s,n) :
                ## if i > s then i am in the outer level of comparision
                if i > s and candidates[i] == candidates[i - 1]:
                    continue
                temp = tracker[:]
                temp.append(candidates[i])
                backtrack(i+1,temp,tot + candidates[i])
        backtrack(0,[],0)
        return res
       
            







        

        