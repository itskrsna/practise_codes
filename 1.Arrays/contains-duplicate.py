from typing import List


class Solution:
    # O(N^2) time, O(1) space
    # def containsDuplicate(self, nums: List[int]) -> bool:
    #     nums.sort()
    #     for i in range(len(nums)):
    #         for k in range(i+1,len(nums)):
    #             if nums[i] == nums[k]:
    #                 return True
    #     return False
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))

if __name__ == "__main__":
    s = Solution()
    print(s.containsDuplicate([1,2,3,4]))