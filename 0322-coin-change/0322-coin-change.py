class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        # coins.sort()
        dp = [float('inf') for i in range(amount+1)] 
        dp[0] = 0
        for i in range(1,amount+1) :
            for coin in coins :
                diff = i - coin
                if diff < 0 :
                    continue 
                dp[i] = min(dp[i],dp[diff]+1)
        
        if dp[amount] != float('inf') :
         return dp[amount]
        return -1
