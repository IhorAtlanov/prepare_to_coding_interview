"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

 

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]

Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Explanation:

There is no string in strs that can be rearranged to form "bat".
The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.
Example 2:

Input: strs = [""]

Output: [[""]]

Example 3:

Input: strs = ["a"]

Output: [["a"]]  
"""
class Solution:
    def groupAnagrams(self, strs):
      dict_anagrams = {}
      
      for word in strs:
        sortedwords = ''.join(sorted(word))
        
        if sortedwords not in dict_anagrams:
          dict_anagrams[sortedwords] = []
        
        dict_anagrams[sortedwords].append(word)
      
      return list(dict_anagrams.values())[::-1]

print(Solution().groupAnagrams(["eat","tea","tan","ate","nat","bat"]))