class Solution(object):
    def dividePlayers(self, skill):
        """
        :type skill: List[int]
        :rtype: int
        """
        skill.sort()
        r = len(skill) -1 
        l = 0
        temp = skill[l] + skill[r]
        sum = 0
        while l < r :
            if skill[l] + skill[r] == temp :
                sum += skill[l] * skill[r]
                l += 1 
                r -= 1
            else :
                return -1
        return sum


