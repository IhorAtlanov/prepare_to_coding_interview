# Brute Force Solution
"""class Solution:
  def productExceptSelf(self, nums: list[int]) -> list[int]:
    ans = []
    nums_range = len(nums)
    product = 1

    for i in range(nums_range):
        for j in range(0, nums_range):
            if j != i:
              product *= nums[j]
        res[i] = product
        product = 1
    return ans"""

# Time Comlexity: O(n^2) 
# Space Complexity: O(n)
  
  
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        prod, zero_cnt = 1, 0
        for num in nums:
            if num:
                prod *= num
            else:
                zero_cnt += 1
                
        if zero_cnt > 1:
          return [0] * n

        res = [0] * n
        for index, number in enumerate(nums):
            if zero_cnt:
                res[index] = 0 if number else prod
            else:
                res[index] = prod // number
        return res
      
      
solution = Solution()
print(solution.productExceptSelf([1, 2, 3, 4]))  # Output: [24, 12, 8, 6]

# Time Comlexity: O(n) 
# Space Complexity: O(n)