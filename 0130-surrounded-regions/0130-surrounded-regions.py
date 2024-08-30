class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        row = len(board)
        col = len(board[0])
        myset = set()
        temp = set()
        self.flag = False
        def dfs(i,j) :
            if i == row or j == col or  (i,j) in myset or board[i][j] == 'X' :
                return 
            ## mark that there is an item for this group reach the edge
            if i+1 == row or j+1 == col or i-1 < 0 or j-1 < 0 :
                self.flag = True
                return
            myset.add((i,j))
            temp.add((i,j))
            dfs(i,j+1)
            dfs(i,j-1)
            dfs(i+1,j)
            dfs(i-1,j)
        count = 0
        for i in range(row) :
            for j in range(col) :
                if board[i][j] == 'O' and (i,j) not in myset :
                    dfs(i,j)
                
                ## turn all the sets into 'X'
                if not self.flag :
                    for pair in temp :
                        board[pair[0]][pair[1]] = 'X'


                ## reset our temp set
                temp = set()
                self.flag = False
        

        