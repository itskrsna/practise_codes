from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans = []
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    ans.append(i)
                    ans.append(j)
        return ans

if __name__ == "__main__":
    s = Solution()
    print(s.twoSum([2, 7, 11, 15], 9))