class Solution(object):
    def robotSim(self, commands, obstacles):
        """
        :type commands: List[int]
        :type obstacles: List[List[int]]
        :rtype: int
        """
        def helper(x,y) :
            return x**2 + y**2
    
        # direction = [(0,1),(1,0),(0,-1),(-1,0)]
        myset = set()
        for obs in obstacles :
            myset.add((obs[0],obs[1]))
        
        hashmap = {
            'N' : (0,1) ,
            'E' : (1,0) ,
            'S' : (0,-1) ,
            'W' : (-1,0)
        }
        directions = ['N','E','S','W']
        curr = 0
        maxi = 0
        curr_position = [0,0]
        for c in commands :
            ## turn right
            if c == -1 :
                curr += 1
                curr %= 4
            ## turn left
            elif c == - 2 :
                curr -= 1
                curr %= 4
            else :    
                new_x , new_y = hashmap[directions[curr]]
                for i in range(c) :
                    curr_position[0] += new_x 
                    curr_position[1] += new_y
                    if tuple(curr_position) in myset :
                            curr_position[0] -= new_x 
                            curr_position[1] -= new_y
                            break
                    maxi = max(maxi,helper(curr_position[0],curr_position[1]))
                    
        return maxi