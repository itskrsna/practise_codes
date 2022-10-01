from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1] * len(nums)
        left = 1
        right =1
        for i in range(len(nums)):
            ans[i] = left
            ans[~i] = right
            left *= nums[i]
            right *= nums[~i]
        return ans
        # ans = []
        # run_all = True
        # while run_all:
        #         zerocount = nums.count(0) 
        #         if zerocount > 1 :
        #                 return [0] * len(nums)                                         
        #         for i in range(len(nums)):
        #             mul = 1
        #             for j in range(len(nums)):
        #                 if i == j:
        #                     continue
        #                 else:
        #                     mul *= nums[j]                                   
        #             if zerocount <= 1 :
        #                 ans.append(mul)
                    
                                                              
        #         if(len(ans) == len(nums)):
        #             run_all = False
        #             return ans


if __name__ == "__main__":
    s = Solution()
    print(s.productExceptSelf(
    [1,2,3,4]))

                