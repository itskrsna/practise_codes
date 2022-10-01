from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        left = 0
        right = 1
        while right < len(prices):
             if prices[left] < prices[right]:
                    max_profit = max(max_profit, prices[right] - prices[left])
             else:
               left = right 
             right += 1                  
        return max_profit
        

        

if __name__ == "__main__":
    s = Solution()
    print(s.maxProfit([7,1,5,3,6,4]))