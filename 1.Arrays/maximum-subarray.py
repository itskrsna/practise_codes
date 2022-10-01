from cmath import inf
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        ans = - inf
        for i in range(len(nums)):
            max_sum = 0
            for j in range(i,len(nums)):
                max_sum += nums[j]
                ans = max(ans,max_sum)
        return ans

if __name__ == "__main__":
    s = Solution()
    print(s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))


