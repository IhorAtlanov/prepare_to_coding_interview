"""
Longest Consecutive Sequence

Given an array of integers nums, return the length of the longest consecutive sequence of elements that can be formed.

A consecutive sequence is a sequence of elements in which each element is exactly 1 greater than the previous element. The elements do not have to be consecutive in the original array.

You must write an algorithm that runs in O(n) time.

Example 1:

Input: nums = [2,20,4,10,3,4,5]

Output: 4
Explanation: The longest consecutive sequence is [2, 3, 4, 5].

Example 2:

Input: nums = [0,3,2,5,4,6,1,1]

Output: 7
Constraints:

0 <= nums.length <= 1000
-10^9 <= nums[i] <= 10^9
"""

nums = [2,20,4,10,3,4,5]

def longestConsecutive(nums: list[int]) -> int:
    new_set = set(nums)
    res = 0

    for num in new_set:
        if (num - 1) not in new_set:
            length = 0
            while (num + length) in new_set:
                length += 1
            res = max(length, res)
    return res
  
print(longestConsecutive(nums))

# Sorted Approach
"""
def longestConsecutive(nums: list[int]) -> int:
    if not nums:
        return 0
    res = 0
    nums.sort()

    curr, streak = nums[0], 0
    i = 0
    while i < len(nums):
        if curr != nums[i]:
            curr = nums[i]
            streak = 0
        while i < len(nums) and nums[i] == curr:
            i += 1
        streak += 1
        curr += 1
        res = max(res, streak)
    return res
"""