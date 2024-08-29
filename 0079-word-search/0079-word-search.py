class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        m  = len(board)
        n = len(board[0])
        string = ""
        myset = set()     
        def backtrack(i,j,string,k) :
            if string == word :
                return  True
            if i == m or i < 0 or j < 0 or j == n  or (i,j) in myset  : 
                return False

            string += board[i][j]

            ## if the current character not equal the character of the word return False
            if word[k] != string[k] :
                return False
                
            myset.add((i,j))
            ## go right - go left - go up - go down 
            flag = backtrack(i,j+1,string,k+1) or backtrack(i,j-1,string,k+1)  or  backtrack(i-1,j,string,k+1) or backtrack(i+1,j,string,k+1) 
            myset.remove((i,j))
            return flag
        
        for i in range(m) :
            for j in range(n) :
                if backtrack(i,j,"",0) :
                    return True
        return False

