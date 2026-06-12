"""
Two Integer Sum II
Medium
Topics
Company Tags
Hints
Given an array of integers numbers that is sorted in non-decreasing order.

Return the indices (1-indexed) of two numbers, [index1, index2], such that they add up to a given target number target and index1 < index2. Note that index1 and index2 cannot be equal, therefore you may not use the same element twice.

There will always be exactly one valid solution.

Your solution must use 
O
(
1
)
O(1) additional space.

Example 1:

Input: numbers = [1,2,3,4], target = 3

Output: [1,2]
Explanation:
The sum of 1 and 2 is 3. Since we are assuming a 1-indexed array, index1 = 1, index2 = 2. We return [1, 2].

Constraints:

2 <= numbers.length <= 1000
-1000 <= numbers[i] <= 1000
-1000 <= target <= 1000
"""

numbers=[2,3,4]
target=6

# Brute Force Solution:
def two_sum_brute_force(nums, target):
  for i in range(len(nums)):
      for j in range(i+1, len(nums)):
          if nums[i] + nums[j] == target:
              return [i+1, j+1]
  return None

print(two_sum_brute_force(numbers, target))

# Binary Search

def two_sum_binary_search(nums, target):
  for i in range(len(nums)):
    complement = target - nums[i]
    l ,r = i + 1, len(nums) - 1
    while l <= r:
      mid = l + (r - l) // 2
      if nums[mid] == complement:
        return [i + 1, mid + 1]
      elif nums[mid] < complement:
        l = mid + 1
      else:
        r = mid - 1
  return None

print(two_sum_binary_search(numbers, target))

# Two Pointers Approach

def two_sum_two_pointers(nums, target):
  l, r = 0, len(nums) - 1

  while l < r:
      curSum = nums[l] + nums[r]

      if curSum < target:
          l += 1
      elif curSum > target:
          r -= 1
      else:
          return [l + 1, r + 1]
  return None

print(two_sum_two_pointers(numbers, target))