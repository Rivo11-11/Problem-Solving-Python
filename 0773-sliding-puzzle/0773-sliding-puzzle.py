class Solution(object):
    def slidingPuzzle(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        adj = {
            0 : [1,3] ,
            1 : [0,2,4],
            2 : [1,5],
            3 : [0,4],
            4 : [1,3,5],
            5 : [2,4]
        }
        
        ## turn the list into string 
        row = len(board) 
        col = len(board[0])
        b_string = ''
        for r in range(row) : 
            for c in range(col) :
                b_string += str(board[r][c])

        target = '123450'
        queue = deque([(b_string,b_string.index('0'),0)])
        visited = set() ## take a  set of string that we visited 
        visited.add(b_string)
        while queue:
            string, index, length = queue.popleft()
            if string == target:
                return length
            l = list(string)
            for neighbour in adj[index]:
                l[neighbour], l[index] = l[index], l[neighbour]
                new_string = "".join(l)  #
                if new_string not in visited:
                    queue.append((new_string, new_string.index('0'), length + 1))
                    visited.add(new_string)
                l[neighbour], l[index] = l[index], l[neighbour]

        return -1  
             