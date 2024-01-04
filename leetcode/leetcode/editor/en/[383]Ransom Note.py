# Given two strings ransomNote and magazine, return true if ransomNote can be 
# constructed by using the letters from magazine and false otherwise. 
# 
#  Each letter in magazine can only be used once in ransomNote. 
# 
#  
#  Example 1: 
#  Input: ransomNote = "a", magazine = "b"
# Output: false
#  
#  Example 2: 
#  Input: ransomNote = "aa", magazine = "ab"
# Output: false
#  
#  Example 3: 
#  Input: ransomNote = "aa", magazine = "aab"
# Output: true
#  
#  
#  Constraints: 
# 
#  
#  1 <= ransomNote.length, magazine.length <= 10⁵ 
#  ransomNote and magazine consist of lowercase English letters. 
#  
# 
#  👍 4726 👎 482


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine_freq = {}
        for c in magazine:
            magazine_freq[c] = magazine_freq.get(c, 0) + 1
        for c in ransomNote:
            magazine_freq[c] = magazine_freq.get(c, 0) - 1
            if magazine_freq[c] < 0:
                return False
        return True
# leetcode submit region end(Prohibit modification and deletion)
