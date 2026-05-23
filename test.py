"""def max_value(nums):
  max_val = nums[0]
  for i in range(1, len(nums)):
    if nums[i] > max_val:
      max_val = nums[i]
  return max_val

print(max_value([-5, -2, -1, -11]))"""


def longest_word(sentence):
  words = sentence.split(" ")
  longest = ""
  
  for i in words:
    if len(i) > len(longest):
      longest = i
  
  return longest

print(longest_word("the quick brown fox jumped over the lazy dog"))