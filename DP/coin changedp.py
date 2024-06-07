'''322. Coin Change
Solved
Medium
Topics
Companies
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

 

Example 1:

Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1'''

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp=[amount+1]*(amount+1)
        dp[0]=0

        for a in range(1,amount+1):
            for c in coins:
                if a-c>=0:
                    dp[a]=min(dp[a],dp[a-c]+1)
        return dp[amount] if dp[amount]!=amount+1 else -1
    
'''[1,3,4,5]
dp[0]=0
dp[1]=1
dp[2]=2..

dp[7]=  1+dp[6]=2
        1=dp[4]=3    min(dp[a],dp[a-c]+1)
        1+dp[3]=2
        1+dp[2]=3 '''